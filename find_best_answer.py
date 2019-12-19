import json
import math
from fuzzywuzzy import process
from fuzzywuzzy.fuzz import token_sort_ratio

TEXT_MATCH_RESULTS = 10
with open("qa.json", "r") as f:
    comments = json.load(f)

qa = {
    comment['question']: comment for comment in comments
}


def get_answer(question):
    result = process.extract(question, qa.keys(), limit=TEXT_MATCH_RESULTS, scorer=token_sort_ratio)
    upvote_weighted = [
        (qa[q], text_score + math.log(qa[q]["score"])) for q, text_score in result
    ]
    upvote_weighted = sorted(upvote_weighted, key=lambda x: -x[1])
    return upvote_weighted[0][0]


if __name__ == '__main__':
    question = input("Ok Boomer, ")
    if not question:
        question = 'find me a job'
        print(question)
    print("=" * 100)
    result = get_answer(question)
    print(result['answer'], result['author'], result['score'])
