# Chap08/youtube_search_video.py
import os
import json
from datetime import datetime
from argparse import ArgumentParser
from apiclient.discovery import build

def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--query')
    parser.add_argument('--n', type=int)
    return parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    api_key = os.environ.get('GOOGLE_API_KEY')
    service = build('youtube',
                    'v3',
                    developerKey=api_key)

    search_feed = service.search()
    search_query = search_feed.list(q=args.query,
                                    part="id,snippet",
                                    maxResults=args.n,
                                    type='channel')
    search_response = search_query.execute()

    print(json.dumps(search_response, indent=4))
    # for item in search_response['items']:
    #     if item['id']['kind'] == 'youtube#video':
    #         print("{}: https://youtube.com/watch?v={}".format(item['snippet']['title'], item['id']['videoId']))
