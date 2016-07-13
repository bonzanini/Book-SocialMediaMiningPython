# Chap08/github_get_user.py
import os
from argparse import ArgumentParser
from github import Github
from github.GithubException import UnknownObjectException

def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--user')
    parser.add_argument('--get-repos', action='store_true', default=False)
    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    client_id = os.environ['GITHUB_CLIENT_ID']
    client_secret = os.environ['GITHUB_CLIENT_SECRET']

    g = Github(client_id=client_id, client_secret=client_secret)

    try:
        user = g.get_user(args.user)
        print("Username: {}".format(args.user))
        print("Full name: {}".format(user.name))
        print("Location: {}".format(user.location))
        print("Number of repos: {}".format(user.public_repos))
        if args.get_repos:
            repos = user.get_repos()
            for repo in repos:
                print("Repo: {} ({} stars)".format(repo.name, repo.stargazers_count))
    except UnknownObjectException:
        print("User not found")
