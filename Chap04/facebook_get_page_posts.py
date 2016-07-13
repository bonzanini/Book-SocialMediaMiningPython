# Chap04/facebook_get_page_posts.py
import os
import json
from argparse import ArgumentParser
import facebook
import requests


def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--page')
    parser.add_argument('--n', default=100, type=int)
    return parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    token = os.environ.get('FACEBOOK_TEMP_TOKEN')

    graph = facebook.GraphAPI(token)
    all_fields = [
        'id',
        'message',
        'created_time',
        'shares',
        'likes.summary(true)',
        'comments.summary(true)'
    ]
    all_fields = ','.join(all_fields)
    posts = graph.get_connections('PacktPub', 'posts', fields=all_fields)

    downloaded = 0
    while True:  # keep paginating
        if downloaded >= args.n:
            break
        try:
            fname = "posts_{}.jsonl".format(args.page)
            with open(fname, 'a') as f:
                for post in posts['data']:
                    downloaded += 1
                    f.write(json.dumps(post)+"\n")
                # get next page
                posts = requests.get(posts['paging']['next']).json()
        except KeyError:
            # no more pages, break the loop
            break
