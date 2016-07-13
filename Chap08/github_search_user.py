# Chap08/github_search_user.py
import os
from argparse import ArgumentParser
from argparse import ArgumentTypeError
from github import Github

def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--query')
    parser.add_argument('--sort',
                        default='followers',
                        type=check_sort_value)
    parser.add_argument('--order',
                        default='desc',
                        type=check_order_value)
    parser.add_argument('--n', default=5, type=int)
    return parser


def check_sort_value(value):
    valid_sort_values = ['followers', 'joined', 'repositories']
    if value not in valid_sort_values:
         raise ArgumentTypeError('"{}" is an invalid value for "sort"'.format(value))
    return value


def check_order_value(value):
    valid_order_values = ['asc', 'desc']
    if value not in valid_order_values:
         raise ArgumentTypeError('"{}" is an invalid value for "order"'.format(value))
    return value


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    client_id = os.environ['GITHUB_CLIENT_ID']
    client_secret = os.environ['GITHUB_CLIENT_SECRET']

    g = Github(client_id=client_id, client_secret=client_secret)

    users = g.search_users(args.query,
                          sort=args.sort,
                          order=args.order)
    for i, u in enumerate(users[:args.n]):
        print("{}) {} ({}) with {} repos ".format(i+1, u.login, u.name, u.public_repos))
