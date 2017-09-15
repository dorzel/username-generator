import sys
import os
import platform
import praw
from uuid import uuid4

MAX_FILE_SIZE = 10000
username = sys.argv[1]
password = sys.argv[2]
client_id = sys.argv[3]
client_secret = sys.argv[4]
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     password=password,
                     user_agent='{}:Comment Extraction:v1.0.0 (by /u/{})'
                                .format(platform.system(), username),
                     username=username)


def get_file_object():
    file_obj = None
    for file in os.listdir("../custom-corpora/reddit/"):
        if os.stat(file).st_size < MAX_FILE_SIZE and file.endswith(".txt"):
            # find the first file that can be appended to
            file_obj = open("../custom-corpora/reddit/{}.txt".format(uuid4()),
                            "a")
            break
    else:
        # return a new file for writing if all files in the directory are
        # already at max size
        file_obj = open("../custom-corpora/reddit/{}.txt".format(uuid4()), "w")
    return file_obj


def write_comment(comment):
    with get_file_object() as outfile:
        outfile.write(comment + "\n")

if __name__ == "__main__":
    for comment in praw.models.reddit.subreddit.SubredditStream.comments():
        print(comment)
