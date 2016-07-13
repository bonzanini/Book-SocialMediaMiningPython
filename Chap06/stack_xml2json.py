# Chap06/stack_xml2json.py
import json
from argparse import ArgumentParser
from bs4 import BeautifulSoup
try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree


def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--xml')
    parser.add_argument('--json')
    parser.add_argument('--clean-post', default=False, action='store_true')
    return parser


def clean_post(doc):
    try:
        doc['Tags'] = doc['Tags'].replace('><', ' ')
        doc['Tags'] = doc['Tags'].replace('<', '')
        doc['Tags'] = doc['Tags'].replace('>', '')
    except KeyError:
        pass
    soup = BeautifulSoup(doc['Body'], 'html.parser')
    doc['Body'] = soup.get_text(" ", strip=True)
    return doc


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    xmldoc = etree.parse(args.xml)
    entity = xmldoc.getroot()
    with open(args.json, 'w') as fout:
        for row in entity:
            doc = dict(row.attrib)
            if args.clean_post:
                doc = clean_post(doc)
            fout.write("{}\n".format(json.dumps(doc)))
