from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hweight.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
      # posts = Post.query.all() グラフを表示
      return render_template('index.html', posts=posts)

    else:
      name = request.from.get('name')
      height = request.from.get('height')
      weight = request.from.get('weight')

      new_post = Post(name=name, height=height, weight=weight)

      db.session.add(new_post)
      db.session.commit()
      return redirect('/')

@app.route('/create')
def create():
    return render_template('create.html')

if __name__ == "__main__":
    app.run(debug=True)