import json

MIN_SCORE = 10
with open("comments.json", "r") as f:
    comments = json.load(f)


def split_newline(question, answer):
    parts = question.split("\n")
    parts = [part for part in parts if part]
    if len(parts) == 2:
        return parts
    return parts[0], "\n".join(parts[1:])


QUOTE_SIGNS = [
    "\"",
    "“",
    "”"
]


def remove_quotes(question, answer):
    for sign in QUOTE_SIGNS:
        question, answer = question.replace(sign, ""), answer.replace(sign, "")
    return question, answer


steps = [
    split_newline,
    remove_quotes
]

for comment in comments:
    if comment['score'] < MIN_SCORE:
        continue
    question, answer = comment['body'], ""
    for step in steps:
        question, answer = step(question, answer)
    print(f"question: {question}\n answer: {answer}")
