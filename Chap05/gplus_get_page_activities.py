# Chap05/gplus_get_page_activities.py
import os
import json
from argparse import ArgumentParser
from apiclient.discovery import build

def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--page')
    parser.add_argument('--max-results', type=int, default=100)
    return parser

if __name__ == '__main__':
    api_key = os.environ.get('GOOGLE_API_KEY')
    parser = get_parser()
    args = parser.parse_args()


    service = build('plus',
                    'v1',
                    developerKey=api_key)

    activity_feed = service.activities()
    activity_query = activity_feed.list(
        collection='public',
        userId=args.page,
        maxResults='100'
    )

    fname = 'activities_{}.jsonl'.format(args.page)
    with open(fname, 'w') as f:
        retrieved_results = 0
        while activity_query and retrieved_results < args.max_results:
            activity_results = activity_query.execute()
            retrieved_results += len(activity_results['items'])
            for item in activity_results['items']:
                f.write(json.dumps(item)+"\n")

            activity_query = service.activities().list_next(activity_query, activity_results)

    # print(json.dumps(activity_results, indent=4))
    # print(activity_results.keys())
