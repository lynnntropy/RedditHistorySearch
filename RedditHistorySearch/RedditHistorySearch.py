import praw
import sys
import re
import os

if len(sys.argv) >= 3:
    username = sys.argv[1]
    search_string = sys.argv[2]
else:
    print "Not enough parameters."
    os._exit(0)

search_regex = re.compile(search_string, re.IGNORECASE)

r = praw.Reddit('Comment History Search by /u/OmegaVesko')

user = r.get_redditor(username)

for comment in user.get_comments(limit=None):
    body = comment.body

    if search_regex.search(body):
        print (u"%s: %s" % (comment.id, body[:50])).encode('utf-8')