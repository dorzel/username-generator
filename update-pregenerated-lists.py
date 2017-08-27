import nltk
import pickle
from collections import defaultdict


def generate_existing_lists():
    """ Populate a dictionary of types of tags with words that belong to that
    tag. This works on any existing corpora in nltk that are tagged.
    """

    existing_word_tags = defaultdict(list)

    # any corpus that has the .tagged_words() method and supports the universal
    # tagset can be used here
    # TODO: make this a general loop instead of having to name all corpora
    for corpus_name in ["treebank", "brown", "nps_chat", "masc_tagged",
                        "switchboard", "timit_tagged"]:
        corpus = getattr(nltk.corpus, corpus_name)
        # append data to tag types in dict
        print("generating lists for '{}' corpus...".format(corpus_name))
        for tag in corpus.tagged_words(tagset='universal'):
            existing_word_tags[tag[-1]].append(tag[0])

    # write results
    with open("pre-generated-lists/existing_word_tags.pkl", "wb") as outfile:
        pickle.dump(existing_word_tags, outfile)

    print("Done. {} total words saved".format(
        sum([len(values) for values in existing_word_tags.values()])))


def generate_custom_lists():
    """ Same as generate_existing_lists, but on custom corpora that reside in
    root/custom_corpora. Write a pickle
    """
    from nltk.corpus import PlaintextCorpusReader
    import os

    custom_word_tags = defaultdict(list)

    for dir in os.listdir("custom-corpora/"):
        print("generating list for custom corpus '{}'".format(dir))
        # if this isn't parsing correctly, you can pass this a custom word
        # tokenizer and a sentence tokenizer
        p1 = PlaintextCorpusReader(root="custom-corpora/{}/".format(dir),
                                   fileids=".txt")
        # tokenize and tag sentences
        p1.sents()
        
    # write results
    with open("pre-generated-lists/custom_word_tags.pkl", "wb") as outfile:
        pickle.dump(custom_word_tags, outfile)

    print("Done. {} total words saved".format(
        sum([len(values) for values in custom_word_tags.values()])))


def get_tags_sentence(sentence):
    """ Returns a list of (word, tag) tuples for every tag that is a noun,
    verb, or adjective for the given sentence.
    """
    tags = nltk.tag.pos_tag(nltk.tokenize.word_tokenize(sentence),
                            tagset='universal',
                            lang='eng')
    return [tag for tag in tags if tag[-1] in ["NOUN", "ADJ", "VERB"]]

if __name__ == "__main__":
    generate_existing_lists()
    generate_custom_lists()
