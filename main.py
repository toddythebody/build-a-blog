from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:build-a-blog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Entry(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    body = db.Column(db.String(2000))

    def __init__(self, name, body, date):
        self.name = name
        self.body = body


@app.route('/')
def index():

    blogPosts = Entry.query.all()

    return render_template('index.html', title="Main Page", posts=blogPosts)

if __name__ == "__main__":
    app.run()
