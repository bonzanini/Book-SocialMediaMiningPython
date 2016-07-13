# Chap02-03/twitter_make_geojson.py
import json
from argparse import ArgumentParser


def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--tweets')
    parser.add_argument('--geojson')
    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    # Read tweet collection and build geo data structure
    with open(args.tweets, 'r') as f:
        geo_data = {
            "type": "FeatureCollection",
            "features": []
        }
        for line in f:
            tweet = json.loads(line)
            try:
                if tweet['coordinates']:
                    geo_json_feature = {
                        "type": "Feature",
                        "geometry": {
                            "type": "Point",
                            "coordinates": tweet['coordinates']['coordinates']
                        },
                        "properties": {
                            "text": tweet['text'],
                            "created_at": tweet['created_at']
                        }
                    }
                    geo_data['features'].append(geo_json_feature)
            except KeyError:
                # Skip if json doc is not a tweet (errors, etc.)
                continue
     
    # Save geo data
    with open(args.geojson, 'w') as fout:
        fout.write(json.dumps(geo_data, indent=4))
