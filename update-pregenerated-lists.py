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
        corpus = getattr(nltk.corpus, corpus_name, False)
        print("generating lists for '{}' corpus...".format(corpus_name))
        if corpus:
            for tag in corpus.tagged_words(tagset='universal'):
                existing_word_tags[tag[-1]].append(tag[0])
        else:
            print("'{}' corpus not found. Downloading...".format(corpus_name))
            nltk.download(corpus_name)

    # write results
    with open("pre-generated-lists/existing_word_tags.pkl", "wb") as outfile:
        pickle.dump(existing_word_tags, outfile)

    print("Done. {} total words saved".format(
        sum([len(values) for values in existing_word_tags.values()])))


def generate_custom_lists():
    """ Same as generate_existing_lists, but on custom corpora that reside in
    root/custom_corpora. Write a pickle file for each corpus. 
    """
    from nltk.corpus import PlaintextCorpusReader
    import os

    for dir in os.listdir("custom-corpora/"):
        print("generating list for custom corpus '{}'".format(dir))
        custom_word_tags = defaultdict(list)
        custom_corpus = PlaintextCorpusReader(
            root="custom-corpora/{}/".format(dir),
            fileids=".*")
        # tokenize and tag sentences
        tags = get_tags_sentence([item for item in custom_corpus.sents()])
        for tag in tags:
            custom_word_tags[tag[-1]].append(tag[0])

        # write results
        with open("pre-generated-lists/custom_word_tags_{}.pkl".format(dir),
                  "wb") as outfile:
            pickle.dump(custom_word_tags, outfile)

        print("Completed dumping of `{}` custom corpus. {} total words saved"
              .format(dir,
                      sum([len(values) for values in custom_word_tags.values()]
                          )))


def get_tags_sentence(sentence):
    """ Returns a list of (word, tag) tuples for every tag that is a noun,
    verb, or adjective for the given sentence. Accepts sentence as a raw string
    or a list of sentences with each "sentence" being a list of words from that
    sentence, as returned by PlainTextCorpusReader.sents(). 
    """
    tags = []
    if isinstance(sentence, str):
        # raw sentence as a string
        tags = nltk.tag.pos_tag(nltk.tokenize.word_tokenize(sentence),
                                tagset='universal',
                                lang='eng')
    elif isinstance(sentence, list):
        # list of sentences, each sentence being a list of words.
        tagged_sents = nltk.tag.pos_tag_sents(sentence,
                                              tagset='universal',
                                              lang='eng')
        for tagged_sent in tagged_sents:
            for tag in tagged_sent:
                tags.append(tag)

    return tags

if __name__ == "__main__":
    generate_existing_lists()
    generate_custom_lists()
