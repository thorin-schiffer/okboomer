import json

from praw.models import MoreComments

REDDIT_USER_AGENT = 'web:okboomer:1.0 by /u/eviltnan'
SUBMISSION_ID = 'e18g6m'
MIN_SCORE = 10
import praw

print("Connecting reddit...")
reddit = praw.Reddit('boomer',
                     user_agent=REDDIT_USER_AGENT)
print("Finding submission...")
submission = reddit.submission(id=SUBMISSION_ID)

print("Finding comments...")
comments = []
# submission.comments.replace_more(limit=None)
for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments):
        continue
    print(top_level_comment.body)
    comments.append({
        "body": top_level_comment.body,
        "score": top_level_comment.score,
        "author": top_level_comment.author.name,
        "permalink": top_level_comment.permalink,
    })

print(f"Done: {len(comments)} comments, writing comments.json")

with open("comments.json", "w") as f:
    json.dump(comments, f)
