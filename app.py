# python -m flask run

# to set up environment:
# Set-ExecutionPolicy Unrestricted -Scope Process
# env\Scripts\activate
# 19:43

from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
# import pandas as pd

from word_ranker import ranker
from words import words_list

from solver_calc import calc

# to activate the virtual environment:  env\Scripts\activate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

remaining_words = words_list

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.String(200), nullable=False)
    recomends = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['GET', 'POST'])
def submit_letters():
    if request.method == 'POST':
        letters = request.form.getlist('letter[]')
        colors = request.form.getlist('color[]')
        guess = ""
        color_out = ""
        for letter in letters:
            guess = guess + letter
        for color in colors:
            if color == "green":
                color_out += str(1)
            elif color == "yellow":
                color_out += str(2)
            else:
                color_out += str(3)
            color_out += ","
        color_out = color_out[:-1]
        is_empty = Todo.query.all() == []
        if is_empty:
            remaining_words = calc(guess.lower(), color_out)
        else:
            print(Todo.query.order_by(Todo.id.desc()).first().recomends)
            last_words = Todo.query.order_by(Todo.id.desc()).first().recomends.split(",")
            print(last_words)
            print(type(last_words))
            remaining_words = calc(guess.lower(), color_out, last_words)
        top_ten = ranker(list(remaining_words))



        new_task = Todo(content=guess, date_created=color_out[:-1], recomends=top_ten)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "there was an issue adding the word"
    else:
        tasks = Todo.query.all()
        return render_template("wordle_template.html", tasks=tasks)

@app.route('/clear/',methods=['POST'])
def clear():
    try:
        table = Todo.query.all()
        for entry in table:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue clearing the table'

if __name__ == '__main__':
    app.run()
