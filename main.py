from flask import Flask, request, render_template
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

    def __init__(self, name, body):
        self.name = name
        self.body = body


@app.route('/')
def index():

    blogPosts = Entry.query.all()

    return render_template('index.html', title="Main Page", posts=blogPosts)

@app.route('/entry')
def entry():
    return render_template('entry.html', title="Make a Post")

@app.route('/posted', methods=['POST', 'GET'])
def posted():

    if request.method == 'POST':
        postName = request.form['name']
        postBody = request.form['body']
        newPost = Entry(postName, postBody)
        db.session.add(newPost)
        db.session.commit()
        postQuery = Entry.query.get(newPost.id)
        return render_template('posted.html', title=postName, postName=postName, postBody=postBody,
            postQuery=postQuery)
    else:
        postId = int(request.args.get('id'))
        postQuery = Entry.query.get(postId)
        Name = postQuery.name

        return render_template('posted.html', title=Name, postQuery=postQuery)

if __name__ == "__main__":
    app.run()
