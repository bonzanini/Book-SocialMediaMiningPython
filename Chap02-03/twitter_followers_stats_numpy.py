# Chap02-03/twitter_followers_stats_numpy.py
import sys
import json
import numpy as np
import time

def usage():
    print("Usage:")
    print("python {} <username>".format(sys.argv[0]))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    screen_name = sys.argv[1]
    followers_file = 'users/{}/followers.jsonl'.format(screen_name)
    friends_file = 'users/{}/friends.jsonl'.format(screen_name)
    with open(followers_file) as f1, open(friends_file) as f2:
        t0 = time.time()
        followers = []
        friends = []
        for line in f1:
            profile = json.loads(line)
            followers.append(profile['screen_name'])
        for line in f2:
            profile = json.loads(line)
            friends.append(profile['screen_name'])
        followers = np.array(followers)
        friends = np.array(friends)
        t1 = time.time()
        mutual_friends = np.intersect1d(friends, followers, assume_unique=True)
        followers_not_following = np.setdiff1d(followers, friends, assume_unique=True)
        friends_not_following = np.setdiff1d(friends, followers, assume_unique=True)
        t2 = time.time()
        print("----- Timing -----")
        print("Initialize data: {}".format(t1-t0))
        print("Set-based operations: {}".format(t2-t1))
        print("Total time: {}".format(t2-t0))
        print("----- Stats -----")
        print("{} has {} followers".format(screen_name, len(followers)))
        print("{} has {} friends".format(screen_name, len(friends)))
        print("{} has {} mutual friends".format(screen_name, len(mutual_friends)))
        print("{} friends are not following {} back".format(len(friends_not_following), screen_name))
        print("{} followers are not followed back by {}".format(len(followers_not_following), screen_name))
