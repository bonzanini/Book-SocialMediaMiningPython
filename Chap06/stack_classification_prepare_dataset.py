# Chap06/stack_classification_prepare_dataset.py
import os
import json
from argparse import ArgumentParser

def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--posts-file')
    parser.add_argument('--tags-file')
    parser.add_argument('--output')
    parser.add_argument('--min-df', type=int, default=10)
    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    valid_tags = []
    with open(args.tags_file, 'r') as f:
        for line in f:
            tag = json.loads(line)
            if int(tag['Count']) >= args.min_df:
                valid_tags.append(tag['TagName'])

    with open(args.posts_file, 'r') as fin, open(args.output, 'w') as fout:
        for line in fin:
            doc = json.loads(line)
            if doc['PostTypeId'] == '1':
                doc_tags = doc['Tags'].split(' ')
                tags_to_store = [tag for tag in doc_tags if tag in valid_tags]
                if tags_to_store:
                    doc['Tags'] = ' '.join(tags_to_store)
                    fout.write("{}\n".format(json.dumps(doc)))


