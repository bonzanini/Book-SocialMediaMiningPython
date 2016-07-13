# Chap05/gplus_activities_keywords.py
import os
import json
from argparse import ArgumentParser
from collections import defaultdict
from collections import Counter
from operator import itemgetter
from math import log
from string import punctuation
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import bigrams

punct = list(punctuation)
all_stopwords = stopwords.words('english') + punct

def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--file',
                        '-f',
                        required=True,
                        help='The .jsonl file with all the activities')
    parser.add_argument('--keywords',
                        type=int,
                        default=3,
                        help='Number of keywords to extract for each post')
    return parser


def clean_html(html):
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(" ", strip=True)
    text = text.replace('\xa0', ' ')
    text = text.replace('\ufeff', ' ')
    text = ' '.join(text.split())
    return text


def preprocess(text, stop=all_stopwords, normalize=True):
    if normalize:
        text = text.lower()
    text = clean_html(text)
    tokens = word_tokenize(text)
    return list(bigrams(tokens))
    # return [tok for tok in tokens if tok not in stop]


def make_idf_matrix(corpus):
    df = defaultdict(int)
    for doc in corpus:
        terms = set(doc)
        for term in terms:
            df[term] += 1
    idf = {}
    for term, term_df in df.items():
        idf[term] = 1 + log(len(corpus) / term_df)
    return idf

def get_keywords(doc, idf, normalize=False):
    tf = Counter(doc)
    if normalize:
        tf = {term: tf_value/len(doc) for term, tf_value in tf.items()}
    tfidf = {term: tf_value*idf[term] for term, tf_value in tf.items()}
    return sorted(tfidf.items(), key=itemgetter(1), reverse=True)


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    with open(args.file) as f:

        posts = []
        for line in f:
            activity = json.loads(line)
            posts.append(preprocess(activity['object']['content']))

    idf = make_idf_matrix(posts)

    for i, post in enumerate(posts):
        keywords = get_keywords(post, idf)
        print("----------")
        print("Content: {}".format(post))
        print("Keywords: {}".format(keywords[:args.keywords]))
