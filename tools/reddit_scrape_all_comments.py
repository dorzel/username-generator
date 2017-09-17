import sys
import os
import platform
import praw
from uuid import uuid4


class SubredditCommentScraper:

    def __init__(self, subreddit, username, password, client_id, client_secret):
        self.subreddit = subreddit
        self.username = username
        self.password = password
        self.client_id = client_id
        self.client_secret = client_secret
        self.file_object = None
        self.max_file_size_bytes = 10000000  # 10MB
        self.base_dir = "../custom-corpora/reddit/{}"
        self.reddit = None

    def _set_file_object(self):
        for file in os.listdir(self.base_dir.format("")):
            if os.stat(self.base_dir.format(file)).st_size < self.max_file_size_bytes \
                    and file.endswith(".txt"):
                if self.file_object is not None:
                    # find the first file that can be appended to
                    if self.file_object.name.split("/")[-1] != file:
                        print("closed open file {} due to size ({} bytes)"
                              .format(self.file_object.name,
                                      os.fstat(self.file_object.fileno())))
                        self.file_object.close()
                        self.file_object = open(self.base_dir.format(file), "a")
                        print("Opening file for appending: {}"
                              .format(self.file_object.name))
                        break
                    else:
                        # don't re-open the file we are already writing to
                        break
                else:
                    # first time run, open the first file found for appending
                    self.file_object = open(self.base_dir.format(file), "a")
                    print("Opening (initial) file for appending: {}"
                          .format(self.file_object.name))
                    break
        else:
            # return a new file for writing if all files in the directory are
            # already at max size or no files yet exist
            self.file_object.close()
            self.file_object = open(self.base_dir
                                    .format(str(uuid4()) + '.txt'), "w")
            print("Opening new file for writing: {}"
                  .format(self.file_object.name))

    def _write_comment(self, comment_body):
        self._set_file_object()
        # split comment into nltk-compatible sentences and write out to file.
        sentences = [sentence.strip() + "." for sentence in
                     comment_body.split(".") if
                     sentence.replace(" ", "").strip().isalnum() and
                     len(sentence.split()) > 1]
        for sentence in sentences:
            self.file_object.write(sentence + "\n")

    def start(self):
        self.reddit = praw.Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            password=self.password,
            user_agent='{}:Comment Extraction:v1.0.0 (by /u/{})'
                       .format(platform.system(), self.username),
            username=self.username)
        try:
            for comment in self.reddit.subreddit(self.subreddit).stream.comments():
                self._write_comment(comment.body)
        except KeyboardInterrupt:
            self.file_object.close()
            print("Done.")

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    client_id = sys.argv[3]
    client_secret = sys.argv[4]
    s1 = SubredditCommentScraper(subreddit="all",
                                 username=username,
                                 password=password,
                                 client_id=client_id,
                                 client_secret=client_secret)
    s1.start()
