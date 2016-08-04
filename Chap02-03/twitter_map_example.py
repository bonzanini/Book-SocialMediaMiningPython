# Chap02-03/twitter_map_example.py
from argparse import ArgumentParser
import folium


def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--map')
    return parser


def make_map(map_file):
    # Custom map
    sample_map = folium.Map(location=[50, 5],
                            zoom_start=5)
    # Marker for London
    london_marker = folium.Marker([51.5, -0.12],
                                  popup='London')
    london_marker.add_to(sample_map)
    # Marker for Paris
    paris_marker = folium.Marker([48.85, 2.35],
                                 popup='Paris')
    paris_marker.add_to(sample_map)
    # Save to HTML file
    sample_map.save(map_file)


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    make_map(args.map)
