import json

from fuzzywuzzy import process
from fuzzywuzzy.fuzz import token_sort_ratio

with open("qa.json", "r") as f:
    comments = json.load(f)

questions = {
    comment['question']: comment['answer'] for comment in comments
}
i = input("Question:")
result = process.extract(i, questions.keys(), limit=1, scorer=token_sort_ratio)
if result:
    print(questions[result[0][0]])
