# Chap02-03/twitter_hashtag_stats.py
import sys
from collections import defaultdict
import json

def get_hashtags(tweet):
    entities = tweet.get('entities', {})
    hashtags = entities.get('hashtags', [])
    return [tag['text'].lower() for tag in hashtags]

def usage():
    print("Usage:")
    print("python {} <filename.jsonl>".format(sys.argv[0]))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    fname = sys.argv[1]
    with open(fname, 'r') as f:
        hashtag_count = defaultdict(int)
        for line in f:
            tweet = json.loads(line)
            hashtags_in_tweet = get_hashtags(tweet)
            n_of_hashtags = len(hashtags_in_tweet)
            hashtag_count[n_of_hashtags] += 1
        
        tweets_with_hashtags = sum([count for n_of_tags, count in hashtag_count.items() if n_of_tags > 0])
        tweets_no_hashtags = hashtag_count[0]
        tweets_total = tweets_no_hashtags + tweets_with_hashtags
        tweets_with_hashtags_percent = "%.2f" % (tweets_with_hashtags / tweets_total * 100)
        tweets_no_hashtags_percent = "%.2f" % (tweets_no_hashtags / tweets_total * 100)
        print("{} tweets without hashtags ({}%)".format(tweets_no_hashtags, tweets_no_hashtags_percent))
        print("{} tweets with at least one hashtag ({}%)".format(tweets_with_hashtags, tweets_with_hashtags_percent))

        for tag_count, tweet_count in hashtag_count.items():
            if tag_count > 0:
                percent_total = "%.2f" % (tweet_count / tweets_total * 100)
                percent_elite = "%.2f" % (tweet_count / tweets_with_hashtags * 100)
                print("{} tweets with {} hashtags ({}% total, {}% elite)".format(tweet_count,
                                                                                 tag_count,
                                                                                 percent_total,
                                                                                 percent_elite))
