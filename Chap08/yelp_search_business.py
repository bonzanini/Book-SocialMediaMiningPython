# Chap08/yelp_search_business.py
from argparse import ArgumentParser
from yelp_client import get_yelp_client

def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--location')
    parser.add_argument('--search')
    parser.add_argument('--language', default='en')
    parser.add_argument('--limit', default=20)
    parser.add_argument('--sort', default=2)
    return parser


if __name__ == '__main__':
    client = get_yelp_client()
    parser = get_parser()
    args = parser.parse_args()

    params = {
        'term': args.search,
        'lang': args.language,
        'limit': args.limit,
        'sort': args.sort
    }

    response = client.search(args.location, **params)
    for business in response.businesses:
        address = ', '.join(business.location.address)
        categories = ', '.join([cat[0] for cat in business.categories])
        print("{} id={} ({}, {}); rated {}; categories {}".format(business.name, business.id,
                                            address,
                                            business.location.postal_code,
                                            business.rating,
                                            categories))