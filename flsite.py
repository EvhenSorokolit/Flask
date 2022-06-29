import sqlite3
import os
from flask import Flask, render_template, request, g, flash,abort
from FDataBase import FDataBase
# config
DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = "sfsfasdfdagdsgdsf"

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row

    return conn


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
        db.commit()
        db.close()


def get_db():
    # connect to db , if it not exist
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
        return g.link_db


@app.route("/")
@app.route("/index")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', menu=dbase.getMenu(),posts= dbase.getPostsAnonce())

@app.route("/post/<alias>")
def showPost(alias):
    db = get_db()
    dbase = FDataBase(db)
    title,post = dbase.getPost(alias)
    if not title:
        abort(404)
    return render_template('post.html',menu=dbase.getMenu(),title=title, post=post)

@app.route("/add_post", methods=["POST", "GET"])
def addPost():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.addPost(request.form['name'], request.form['post'], request.form['url'])
            if not res:
                flash('Ошибка добалвения статьи', category='error')
            else:
                flash(' Статья успешно добавлена',category='success')
        else:
            flash('Ошибка добалвения статьи', category='error')
    return render_template('add_post.html', menu=dbase.getMenu(), title="Добавление статьи")


@app.teardown_appcontext
def close_db(error):
    #close connection if it exist
    if hasattr(g, 'link_db'):
        g.link_db.close()

if __name__ == "__main__":
    app.run(debug=True)