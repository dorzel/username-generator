import sys
import os
import platform
import praw
from uuid import uuid4

MAX_FILE_SIZE = 10000000  # 10 MB
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
    base_dir = "../custom-corpora/reddit/{}"
    for file in os.listdir(base_dir.format("")):
        if os.stat(base_dir.format(file)).st_size < MAX_FILE_SIZE and \
                file.endswith(".txt"):
            # find the first file that can be appended to
            file_obj = open(base_dir.format(file), "a")
            break
    else:
        # return a new file for writing if all files in the directory are
        # already at max size
        file_obj = open(base_dir.format(str(uuid4()) + '.txt'), "w")
    return file_obj


def write_comment(comment_body):
    # split comment into nltk-compatible sentences and write out to file.
    # TODO: don't open the file for every single write...
    with get_file_object() as outfile:
        sentences = [sentence.strip() + "." for sentence in
                     comment_body.split(".") if
                     sentence.replace(" ", "").strip().isalnum() and
                     len(sentence.split()) > 1]
        for sentence in sentences:
            outfile.write(sentence + "\n")

if __name__ == "__main__":
    try:
        for comment in reddit.subreddit("all").stream.comments():
            write_comment(comment.body)
    except KeyboardInterrupt:
        print("Done.")
