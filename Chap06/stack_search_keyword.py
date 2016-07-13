# Chap06/stack_search_keyword.py
import os
import json
from argparse import ArgumentParser
from stackexchange import Site
from stackexchange import StackOverflow


def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--tags')
    parser.add_argument('--n', type=int, default=20)
    return parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    my_key = os.environ.get('STACK_KEY')
    
    so = Site(StackOverflow, my_key)
    questions = so.questions(tagged=args.tags, pagesize=20)[:args.n]

    for i, item in enumerate(questions):
        print("{}) {} by {}".format(i,
                                    item.title,
                                    item.owner.display_name))
