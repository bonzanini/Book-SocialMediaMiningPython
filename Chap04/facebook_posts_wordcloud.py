# Chap04/facebook_posts_wordcloud.py
import os
import json
from argparse import ArgumentParser
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from wordcloud import WordCloud


def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--page')
    return parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    fname = "posts_{}.jsonl".format(args.page)

    all_posts = []
    with open(fname) as f:
        for line in f:
            post = json.loads(line)
            all_posts.append(post.get('message', ''))
    text = ' '.join(all_posts)
    stop_list = ['save', 'free', 'today', 'get', 'title', 'titles', 'bit', 'ly']
    stop_list.extend(stopwords.words('english'))
    wordcloud = WordCloud(stopwords=stop_list).generate(text)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig('wordcloud_{}.png'.format(args.page))
