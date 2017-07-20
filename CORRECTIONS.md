Known Errors and Corrections
============================


Even though I tried my best to deliver the highest quality for the final version of the book, and I've received some great help from reviewers and editors, some (hopefully minor) errors still made it into the final product.

This page contains a list of known errors and related corrections.

If you find an error that is not listed here, please open a GitHub issue with a short description of the problem.

---

p. 40

The second example using the `TweetTokenizer` has a wrong reference to a non-existing `TwitterTokenizer`, and should be fixed as follows:

    >>> from nltk.tokenize import TweetTokenizer
    >>> tokenizer = TweetTokenizer()

---

p. 148

The script `facebook_get_page_posts.py` uses the hard-coded string `'PacktPub'`, instead it should
use the command line argument `args.page` as follows:

    posts = graph.get_connections(args.page, 'posts', fields=all_fields)

Credits: [Andre Logunov](https://github.com/capissimo)

---



