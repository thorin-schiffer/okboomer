import json

REDDIT_USER_AGENT = 'web:okboomer:1.0 by /u/eviltnan'
SUBMISSION_ID = 'e18g6m'
import praw

print("Connecting reddit...")
reddit = praw.Reddit('boomer',
                     user_agent=REDDIT_USER_AGENT)
print("Finding submission...")
submission = reddit.submission(id=SUBMISSION_ID)

print("Finding comments...")
comments = []
submission.comments.replace_more(limit=None)
for top_level_comment in submission.comments:
    try:
        comments.append({
            "body": top_level_comment.body,
            "score": top_level_comment.score,
            "author": top_level_comment.author.name,
            "permalink": top_level_comment.permalink,
        })
    except Exception as ex:
        print(f"ERROR: {ex}")
        continue

print(f"Done: {len(comments)} comments, writing comments.json")

with open("comments.json", "w") as f:
    json.dump(comments, f)
