import os
import sys
from reddit_scrape_all_comments import SubredditCommentScraper


class PokemonCommentScraper(SubredditCommentScraper):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base_dir = os.path.abspath(
            os.path.join(__file__, "../../custom-corpora/pokemon/{}"))


if __name__ == "__main__":
    try:
        username = sys.argv[1]
        password = sys.argv[2]
        client_id = sys.argv[3]
        client_secret = sys.argv[4]
    except:
        print("Usage: <username> <password> <client_id> <client_secret>")
    else:
        p1 = PokemonCommentScraper(subreddit="pokemon",
                                   username=username,
                                   password=password,
                                   client_id=client_id,
                                   client_secret=client_secret)
        p1.start()
