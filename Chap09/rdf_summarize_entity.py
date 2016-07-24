# Chap09/rdf_summarize_entity.py
from argparse import ArgumentParser
import rdflib

def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--entity')
    return parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    entity_url = 'http://dbpedia.org/resource/{}'.format(args.entity)

    g = rdflib.Graph()
    g.parse(entity_url)

    disambiguate_url = 'http://dbpedia.org/ontology/wikiPageDisambiguates'
    query = (rdflib.URIRef(entity_url),
             rdflib.URIRef(disambiguate_url),
             None)
    disambiguate = list(g.triples(query))
    if len(disambiguate) > 1:
        print("The resource {}:".format(entity_url))
        for subj, pred, obj in disambiguate:
            print('... may refer to: {}'.format(obj))
    else:
        query = (rdflib.URIRef(entity_url),
                 rdflib.URIRef('http://dbpedia.org/ontology/abstract'),
                 None)
        abstract = list(g.triples(query))
        for subj, pred, obj in abstract:
            if obj.language == 'en':
                print(obj)
