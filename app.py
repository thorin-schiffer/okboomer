import random

from flask import Flask, render_template, request

from find_best_answer import get_answer, questions

app = Flask(__name__)

RANDOM_FIRST = 50


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        question = random.choice(questions[:RANDOM_FIRST])
        return render_template('main.html', question=question)
    else:
        question = request.form['question']
        return render_template('main.html', question=question, comment=get_answer(question))
