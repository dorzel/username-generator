Username Generator
=================

Generates a random username given format from the user.

You can specify what format you want to use by giving the order and type
of chunks of the username.

- A - Adjective
- N - Noun
- V - Verb

## Getting started

First we'll generate some pickle files that need to be in the
`pre-generated-lists/` directory. This only needs to be done the first
time or when you update a custom corpus.

Run:

- `pip install -r requirements.txt`
- `python update-pregenerated-lists.py`

This will generate tagged word lists for every built in corpus that is eligible in ntlk,
as well as any custom corpus in `custom-corpora/`.



## Sample output:

By default, the username generated will be of the form A N, or AdjectiveNoun.

```
dorzel@nio-mbp-dorzel: username-generator$ python generate_username.py
BronchialBargain
dorzel@nio-mbp-dorzel: username-generator$ python generate_username.py
RelativeRefrigerator
dorzel@nio-mbp-dorzel: username-generator$ python generate_username.py
AngryMauch
dorzel@nio-mbp-dorzel: username-generator$ python generate_username.py
FirmerThought
dorzel@nio-mbp-dorzel: username-generator$ python generate_username.py
AtomicRefrigeration
```

You can also specify exactly what you want the username to look like:

```
dorzel@nio-mbp-dorzel: username-generator$ python generate_username.py A N A N
ManySympathyBiggerHotel
dorzel@nio-mbp-dorzel: username-generator$ python generate_username.py A N A N
WaryAssistanceSameApproach
dorzel@nio-mbp-dorzel: username-generator$ python generate_username.py A N A N
WrongGloriesScalarKatie
```

You can also specify A,N,V from a specific custom corpus (body of text)
in the `custom-corpora/` directory. For instance, if I have a directory
called `custom-corpora/pokemon/`, I can specify by:

`python generate_username.py pokemon-N`
or
`python generate_username.py pokemon-V`

```
dorzel@nio-mbp-dorzel: username-generator$ python generate_username.py A pokemon-N
GladPikachu
dorzel@nio-mbp-dorzel: username-generator$ python generate_username.py A pokemon-N
SubjectSquirtle
dorzel@nio-mbp-dorzel: username-generator$ python generate_username.py A pokemon-N
CompetitivePokeballs
dorzel@nio-mbp-dorzel: username-generator$ python generate_username.py A pokemon-N
MuchPokemart
dorzel@nio-mbp-dorzel: username-generator$ python generate_username.py A pokemon-N
DefensiveBulbasaur
```

## Adding your own custom corpora

If you would like to add a body of text to be collected and considered when creating a username,
make a directory in `custom-corpora/`. Inside the directory you can create plain text files
that contain any text you wish. The username generator will automatically tag the words in the
text files upon a `python update-pregenerated-lists.py`. This works best if each line in the
text files are whole sentences.


### Scraping data into custom corpora

In the `tools/` dir, there are different scripts that will scrape data into .txt files in the
`custom-corpora/` dir.

#### Reddit scraping tool

To add data to the reddit custom corpus, run reddit_scrape_comments.py with the following arguments:

`python reddit_scrape_comments.py <reddit_username> <reddit_password> <client_id> <client_secret>`

`client_id` and `client_secret` can both be found (assuming you have created a reddit account) at:

https://www.reddit.com/prefs/apps

Create an app on that page and grab the secret and id from the page.


Ideas:

- make a twitter bot that names animals when people post pictures of animals
- be able to specify different types of usernames, e.g.: unusual, angry, happy
- be able to set a part of the username beforehand:
    - `python generate_username.py A Dog NV`
- output N names in a row, given by the user
