# Chap06/stack_classification_user_input.py
import sys
import json
import pickle
from argparse import ArgumentParser


def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--model')
    return parser

def exit():
    print("Goodbye.")
    sys.exit()


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    with open(args.model, 'rb') as f:
        model = pickle.load(f)
    classifier = model['classifier']
    vectorizer = model['vectorizer']
    mlb = model['mlb']

    while True:
        print("Type your question, or type \"exit\" to quit.")
        user_input = input('> ')
        if user_input == 'exit':
            exit()
        else:
            X = vectorizer.transform([user_input])
            print("Question: {}".format(user_input))
            prediction = classifier.predict(X)
            labels = mlb.inverse_transform(prediction)[0]
            labels = ', '.join(labels)
            if labels:
                print("Predicted labels: {}".format(labels))
            else:
                print("No label available for this question")
