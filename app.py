from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
# to activate the virtual environment:  env\Scripts\activate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.String(200), nullable=False)
    recomends = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['GET', 'POST'])
def submit_letters():
    if request.method == 'POST':
        letters = request.form.getlist('letter[]')
        guess = ""
        for letter in letters:
            guess = guess + letter
        print(guess)

        new_task = Todo(content=guess, date_created="guess_printed", recomends="top_10")
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "there was an issue adding the word"
    else:
        tasks = Todo.query.all()
        return render_template("wordle_template.html", tasks=tasks)

    # return render_template('wordle_template.html')

if __name__ == '__main__':
    app.run()
