# Chap07/blogs_rss_get_posts.py
import json
from argparse import ArgumentParser
import feedparser

def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--rss-url')
    parser.add_argument('--json')
    return parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    feed = feedparser.parse(args.rss_url)
    if feed.entries:
        with open(args.json, 'w') as f:
            for item in feed.entries:
                f.write(json.dumps(item)+"\n")
