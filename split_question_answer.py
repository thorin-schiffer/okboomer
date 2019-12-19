import json

MIN_SCORE = 10
with open("comments.json", "r") as f:
    comments = json.load(f)


def split(question, answer):
    parts = question.split("\n")
    if len(parts) == 1:
        parts = question.split("  ")
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


def remove_edit(question, answer):
    if "edit:" in answer.lower():
        to = answer.lower().index("edit:")
        answer = answer[to + 5:]
    return question, answer


def remove_ok_boomer(question, answer):
    if "boomer" in question.lower():
        to = question.lower().index("boomer")
        question = question[to + 6:]
        question = question.strip()
        if question[0] in [".", ",", ":", " "]:
            question = question[1:]
        question = question.strip()
        question = question.capitalize()
    return question, answer


steps = [
    split,
    remove_quotes,
    remove_edit,
    remove_ok_boomer
]

parsed_comments = []
for comment in comments:
    if comment['score'] < MIN_SCORE:
        continue
    question, answer = comment['body'], ""
    for step in steps:
        question, answer = step(question, answer)

    if not question or not answer:
        continue

    comment['question'] = question
    comment['answer'] = answer
    parsed_comments.append(comment)

with open("qa.json", "w") as f:
    json.dump(parsed_comments, f)
