import pickle
import os
from random import choice
from sys import argv

# a dict of each corpus: {"corpus_name": corpus_dict, ...}
corpora_dict = {}


def load_tag_pickles():
    for filename in os.listdir("pre-generated-lists/"):
        if filename.endswith(".pkl"):
            corpus_name = filename.split("_")[-1].rstrip(".pkl")
            # assuming pkl has a single defaultdict inside
            with open("pre-generated-lists/{}".format(filename), "rb") as tag_pickle:
                corpus_dict = pickle.load(tag_pickle)
                corpora_dict[corpus_name] = corpus_dict


def select_data(segment):
    """ Select relevant tags based on what was specified from the cli. """
    char_mapping = {"V": "VERB", "N": "NOUN", "A": "ADJ"}

    if len(segment) > 1:
        # trying to specify a certain corpus like "Pokemon-N"
        corpus_name = segment.split('-')[0]
        tag_type = segment.split('-')[-1]
        return choice(corpora_dict[corpus_name][char_mapping[tag_type]])
    else:
        # just a regular N,V,A, etc. Collect all data here.
        tags = []
        for corpus_dict in corpora_dict.values():
            tags.extend(corpus_dict[char_mapping[segment]])
        return choice(tags)


def generate_username(name_format):
    """ Generates a username with the given format, choosing from any
    combination of V,N,A (Verb, Noun, Adjective)
    """
    username = ""
    for segment in name_format:
        name_chunk = select_data(segment)
        username = username + name_chunk.capitalize()

    return username

if __name__ == "__main__":
    if len(argv) > 1:
        name_format = argv[1:]
    else:
        name_format = ["A", "N"]
    load_tag_pickles()
    print(generate_username(name_format=name_format))
