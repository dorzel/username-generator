import sys
from reddit_scrape_all_comments import SubredditCommentScraper


class PokemonCommentScraper(SubredditCommentScraper):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base_dir = "../custom-corpora/pokemon/{}"


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    client_id = sys.argv[3]
    client_secret = sys.argv[4]
    p1 = PokemonCommentScraper(subreddit="pokemon",
                               username=username,
                               password=password,
                               client_id=client_id,
                               client_secret=client_secret)
    p1.start()
