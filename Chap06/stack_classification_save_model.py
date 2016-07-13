# Chap06/stack_classification_save_model.py
import json
import pickle
from datetime import datetime
from argparse import ArgumentParser
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer


def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--questions')
    parser.add_argument('--output')
    parser.add_argument('--max-df', default=1.0, type=float)
    parser.add_argument('--min-df', default=1, type=int)
    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    stop_list = stopwords.words('english')

    all_questions = []
    all_labels = []
    with open(args.questions, 'r') as f:
        for line in f:
            doc = json.loads(line)
            question = "{} {}".format(doc['Title'], doc['Body'])
            all_questions.append(question)
            all_labels.append(doc['Tags'].split(' '))

    vectorizer = TfidfVectorizer(min_df=args.min_df,
                                 stop_words=stop_list,
                                 max_df=args.max_df)
    X = vectorizer.fit_transform(all_questions)
    mlb = MultiLabelBinarizer()
    y = mlb.fit_transform(all_labels)

    classifier = OneVsRestClassifier(LinearSVC())

    classifier.fit(X, y)
    model_to_save = {
        'classifier': classifier,
        'vectorizer': vectorizer,
        'mlb': mlb,
        'created_at': datetime.today().isoformat()
    }
    with open(args.output, 'wb') as f:
        pickle.dump(model_to_save, f)
