# Chap04/facebook_get_my_posts.py
import os
import json
import facebook
import requests


if __name__ == '__main__':
    token = os.environ.get('FACEBOOK_TEMP_TOKEN')

    graph = facebook.GraphAPI(token)
    posts = graph.get_connections('me', 'posts', fields='message,created_time,description,caption,link,place,status_type,shares')
    while True:  # keep paginating
        try:
            with open('my_posts.jsonl', 'a') as f:
                for post in posts['data']:
                    f.write(json.dumps(post)+"\n")
                # get next page
                posts = requests.get(posts['paging']['next']).json()
        except KeyError:
            # no more pages, break the loop
            break
