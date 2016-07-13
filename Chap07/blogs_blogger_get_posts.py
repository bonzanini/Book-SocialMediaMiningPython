# Chap07/blogs_blogger_get_posts.py
import os
import json
from argparse import ArgumentParser
from apiclient.discovery import build

def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--url')
    parser.add_argument('--posts', type=int, default=20)
    parser.add_argument('--output')
    return parser


class BloggerClient(object):

    def __init__(self, api_key):
        self.service = build('blogger',
                             'v3',
                             developerKey=api_key)

    def get_posts(self, blog_url, n_posts):
        blog_service = self.service.blogs()
        blog = blog_service.getByUrl(url=blog_url).execute()
        posts = self.service.posts()
        request = posts.list(blogId=blog['id'])
        all_posts = []
        while request and len(all_posts) <= n_posts:
            posts_doc = request.execute()
            try:
                for post in posts_doc['items']:
                    all_posts.append(post)
            except KeyError:
                break
            request = posts.list_next(request, posts_doc)
        return all_posts[:n_posts]


if __name__ == '__main__':
    api_key = os.environ.get('GOOGLE_API_KEY')
    parser = get_parser()
    args = parser.parse_args()

    blogger = BloggerClient(api_key)

    posts = blogger.get_posts(args.url, args.posts)

    with open(args.output, 'w') as f:
        for post in posts:
            f.write(json.dumps(post)+"\n")
