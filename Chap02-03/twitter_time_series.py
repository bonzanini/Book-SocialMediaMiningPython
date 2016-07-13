# Chap02-03/twitter_time_series.py
import sys
import json
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import pandas as pd
import numpy as np
import pickle

if __name__ == '__main__':
    fname = sys.argv[1]

    with open(fname, 'r') as f:
        all_dates = []
        for line in f:
            tweet = json.loads(line)
            all_dates.append(tweet.get('created_at'))
        ones = np.ones(len(all_dates))
        idx = pd.DatetimeIndex(all_dates)
        # the actual series (at series of 1s for the moment)
        my_series = pd.Series(ones, index=idx)

        # Resampling / bucketing into 1-minute buckets
        per_minute = my_series.resample('1Min', how='sum').fillna(0)
        print(my_series.head())
        print(per_minute.head())
        
        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_title("Tweet Frequencies")
        
        hours = mdates.MinuteLocator(interval=20)
        date_formatter = mdates.DateFormatter('%H:%M')

        datemin = datetime(2015, 10, 31, 15, 0)
        datemax = datetime(2015, 10, 31, 18, 0)

        ax.xaxis.set_major_locator(hours)
        ax.xaxis.set_major_formatter(date_formatter)
        ax.set_xlim(datemin, datemax)
        max_freq = per_minute.max()
        ax.set_ylim(0, max_freq)
        ax.plot(per_minute.index, per_minute)

        plt.savefig('tweet_time_series.png')
