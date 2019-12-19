from flask import Flask, render_template, request

from find_best_answer import get_answer

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('main.html')
    else:
        question = request.form['question']
        return render_template('main.html', question=question, comment=get_answer(question))
