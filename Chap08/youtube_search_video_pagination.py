# Chap08/youtube_search_video_pagination.py
import os
import json
from argparse import ArgumentParser
from apiclient.discovery import build

def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--query')
    parser.add_argument('--n', default=50, type=int)
    parser.add_argument('--output')
    return parser


class YoutubeClient(object):

    def __init__(self, api_key):
        self.service = build('youtube',
                             'v3',
                             developerKey=api_key)

    def search_video(self, query, n_results):
        search = self.service.search()
        request = search.list(q=query,
                              part="id,snippet",
                              maxResults=n_results,
                              type='video')
        all_results = []
        while request and len(all_results) <= n_results:
            response = request.execute()
            try:
                for video in response['items']:
                    all_results.append(video)
            except KeyError:
                break
            request = search.list_next(request, response)
        return all_results[:n_results]


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    api_key = os.environ.get('GOOGLE_API_KEY')

    youtube = YoutubeClient(api_key)
    videos = youtube.search_video(args.query, args.n)

    with open(args.output, 'w') as f:
        for video in videos:
            f.write(json.dumps(video)+"\n")

    