# Chap01/demo_gensim.py
from gensim.summarization import summarize
import sys

fname = sys.argv[1]

with open(fname, 'r') as f:
    content = f.read()
    summary = summarize(content, split=True, word_count=100)
    for i, sentence in enumerate(summary):
        print("%d) %s" % (i+1, sentence))
