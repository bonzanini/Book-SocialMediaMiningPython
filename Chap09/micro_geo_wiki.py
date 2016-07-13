# Chap09/micro_geo_wiki.py
from argparse import ArgumentParser
import mf2py

def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--url')
    return parser


def get_geo(doc):
    coords = []
    for d in doc['items']:
        try:
            data = {
                'name': d['properties']['name'][0],
                'geo': d['properties']['geo'][0]['value']
            }
            coords.append(data)
        except (IndexError, KeyError):
            pass
    return coords


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    doc = mf2py.parse(url=args.url, html_parser='lxml')
    coords = get_geo(doc)
    for item in coords:
        print(item)
