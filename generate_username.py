from random import choice
from sys import argv
import pickle

tagged_words = None


def load_tag_pickles():
    global tagged_words
    with open("pre-generated-lists/existing_word_tags.pkl", "rb") as tag_pickle:
        tagged_words = pickle.load(tag_pickle)


def generate_username(name_format):
    """ Generates a username with the given format, choosing from any
    combination of V,N,A (Verb, Noun, Adjective)
    """
    username = ""
    char_mapping = {"V": "VERB", "N": "NOUN", "A": "ADJ"}
    for char in name_format:
        name_chunk = choice(tagged_words[char_mapping[char]])
        username = username + name_chunk.capitalize()

    return username

if __name__ == "__main__":
    if len(argv) > 1:
        name_format = argv[1]
    else:
        name_format = "AN"
    load_tag_pickles()
    print(generate_username(name_format=name_format))
