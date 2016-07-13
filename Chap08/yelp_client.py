# Chap08/yelp_client.py
import os
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator


def get_yelp_client():
    auth = Oauth1Authenticator(
        consumer_key=os.environ['YELP_CONSUMER_KEY'],
        consumer_secret=os.environ['YELP_CONSUMER_SECRET'],
        token=os.environ['YELP_TOKEN'],
        token_secret=os.environ['YELP_TOKEN_SECRET']
    )

    client = Client(auth)
    return client
