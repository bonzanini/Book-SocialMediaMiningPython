# Chap07/blogs_wp_get_posts.py
import json
from argparse import ArgumentParser
import requests


API_BASE_URL = 'https://public-api.wordpress.com/rest/v1.1'

def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--domain')
    parser.add_argument('--posts', type=int, default=20)
    parser.add_argument('--output')
    return parser

def get_posts(domain, n_posts=20):
    url = "{}/sites/{}/posts".format(API_BASE_URL, domain)
    next_page = None
    posts = []
    while len(posts) <= n_posts:
        payload = {'page_handle': next_page}
        response = requests.get(url, params=payload)
        response_data = response.json()
        for post in response_data['posts']:
            posts.append(post)
        next_page = response_data['meta'].get('next_page', None)
        if not next_page:
            break
    return posts[:n_posts]


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    posts = get_posts(args.domain, args.posts)

    with open(args.output, 'w') as f:
        for i, post in enumerate(posts):
            f.write(json.dumps(post)+"\n")

"""
def similarity(w1, w2, sim=wn.path_similarity):
  synsets1 = wn.synsets(w1)
  synsets2 = wn.synsets(w2)
  sim_scores = []
  for synset1 in synsets1:
    for synset2 in synsets2:
      score = sim(synset1, synset2)
      if score:
        sim_scores.append(score)
      else:
        sim_scores.append(0)
  if len(sim_scores) == 0:
    return 0
  else:
    return max(sim_scores)
"""