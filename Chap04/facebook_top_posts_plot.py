# Chap04/facebook_top_posts_plot.py
import json
from argparse import ArgumentParser
import numpy as np
import pandas as pd
import dateutil.parser
import matplotlib.pyplot as plt
from datetime import datetime


def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--page')
    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    fname = "posts_{}.jsonl".format(args.page)

    all_posts = []
    n_likes = []
    n_shares = []
    n_comments = []
    n_all = []
    with open(fname) as f:
        for line in f:
            post = json.loads(line)
            created_time = dateutil.parser.parse(post['created_time'])
            n_likes.append(post['likes']['summary']['total_count'])
            n_comments.append(post['comments']['summary']['total_count'])
            try:
                n_shares.append(post['shares']['count'])
            except KeyError:
                n_shares.append(0)
            n_all.append(n_likes[-1] + n_shares[-1] + n_comments[-1])
            all_posts.append(created_time.strftime('%H:%M:%S'))

        idx = pd.DatetimeIndex(all_posts)
        data = {
            'likes': n_likes,
            'comments': n_comments,
            'shares': n_shares,
            'all': n_all
        }
        my_series = pd.DataFrame(data=data, index=idx)

        # Resampling into 1-hour buckets
        per_hour = my_series.resample('1h', how='sum').fillna(0)    
        
        # Plotting
        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_title("Interaction Frequencies")
        width = 0.8
        ind = np.arange(len(per_hour['all']))
        plt.bar(ind, per_hour['all'])
        tick_pos = ind + width / 2
        labels = []
        for i in range(24):
            d = datetime.now().replace(hour=i, minute=0)
            labels.append(d.strftime('%H:%M'))
        plt.xticks(tick_pos, labels, rotation=90)
        plt.savefig('interactions_per_hour.png')
