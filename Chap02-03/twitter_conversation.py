# Chap02-03/twitter_conversation.py
import sys
import json
from operator import itemgetter
import networkx as nx

def usage():
    print("Usage:")
    print("python {} <filename>".format(sys.argv[0]))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    fname = sys.argv[1]
    with open(fname) as f:
        graph = nx.DiGraph()
        for line in f:
            tweet = json.loads(line)
            if 'id' in tweet:
                graph.add_node(tweet['id'],
                               tweet=tweet['text'],
                               author=tweet['user']['screen_name'],
                               created_at=tweet['created_at'])
                if tweet['in_reply_to_status_id']:
                    reply_to = tweet['in_reply_to_status_id']
                    if tweet['in_reply_to_status_id'] in graph \
                    and tweet['user']['screen_name'] != graph.node[reply_to]['author']:
                        graph.add_edge(tweet['in_reply_to_status_id'], tweet['id'])
        print(nx.info(graph))

        sorted_replied = sorted(graph.degree_iter(), key=itemgetter(1), reverse=True)
        most_replied_id, replies = sorted_replied[0]
        print("Most replied tweet ({} replies):".format(replies))
        print(graph.node[most_replied_id])

        print("Longest discussion:")
        longest_path = nx.dag_longest_path(graph)
        for tweet_id in longest_path:
            node = graph.node[tweet_id]
            print("{} (by {} at {})".format(node['tweet'],
                                            node['author'],
                                            node['created_at']))
