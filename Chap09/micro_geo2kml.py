# Chap09/micro_geo2kml.py
from argparse import ArgumentParser
import mf2py
from pykml.factory import KML_ElementMaker as KML
try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree

def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--url')
    parser.add_argument('--output')
    parser.add_argument('--n', default=20)
    return parser


def get_geo(doc):
    coords = []
    for d in doc['items']:
        try:
            data = {
                'name': d['properties']['name'][0],
                'geo': d['properties']['geo'][0]['value']
            }
            coords.append(data)
        except (IndexError, KeyError):
            pass
    return coords


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    doc = mf2py.parse(url=args.url)
    coords = get_geo(doc)
    folder = KML.Folder()
    for item in coords[:args.n]:
        lat, lon = item['geo'].split('; ')
        place_coords = ','.join([lon, lat])
        place = KML.Placemark(
            KML.name(item['name']),
            KML.Point(KML.coordinates(place_coords))
        )
        folder.append(place)

    with open(args.output, 'w') as fout:
        xml = etree.tostring(folder, pretty_print=True).decode('utf8')
        fout.write(xml)
