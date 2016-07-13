# Chap08/yelp_get_business.py
from argparse import ArgumentParser
from yelp_client import get_yelp_client

def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--id')
    parser.add_argument('--language', default='en')
    return parser


if __name__ == '__main__':
    client = get_yelp_client()
    parser = get_parser()
    args = parser.parse_args()

    params = {
        'lang': args.language
    }

    response = client.get_business(args.id, **params)
    business = response.business
    print("Review count: {}".format(business.review_count))
    for review in business.reviews:
        print("{} (by {})".format(review.excerpt, review.user.name))