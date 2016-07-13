# Chap06/stack_search_user.py
import os
import json
from argparse import ArgumentParser
from argparse import ArgumentTypeError
from stackexchange import Site
from stackexchange import StackOverflow


def check_sort_value(value):
    valid_sort_values = [
        'reputation',
        'creation',
        'name',
        'modified'
    ]
    if value not in valid_sort_values:
         raise ArgumentTypeError("{} is an invalid sort value".format(value))
    return value


def check_order_value(value):
    valid_order_values = ['asc', 'desc']
    if value not in valid_order_values:
        raise ArgumentTypeError("{} is an invalid order value".format(value))
    return value


def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--name')
    parser.add_argument('--sort', default='reputation', type=check_sort_value)
    parser.add_argument('--order', default='desc', type=check_order_value)
    parser.add_argument('--n', type=int, default=20)
    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    my_key = os.environ.get('STACK_KEY')
    
    so = Site(StackOverflow, my_key)

    users = so.users(inname=args.name,
                     sort=args.sort,
                     order=args.order)
    users = users[:args.n]

    for i, user in enumerate(users):
        print("{}) {}, reputation {}, joined {}".format(i,
                                                        user.display_name,
                                                        user.reputation,
                                                        user.creation_date))
