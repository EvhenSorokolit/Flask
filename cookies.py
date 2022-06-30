import sqlite3
import os
from flask import Flask, render_template, request, g, flash, abort, make_response

app = Flask(__name__)

menu = [{"name": "Главня", "url": "/"},
        {"name": "Добавить сатью", "url": "add_post"}]


@app.route("/")
def index():
    return "<h1> Main PAge </h1>"
@app.route("/login")
def login():
    log = ""
    if request.cookies.get('logged'):
        log = request.cookies.get('logged')

    res = make_response(f"<h1>Форма авторизации</h1><p> Logged: {log}")
    res.set_cookie("logged", "yes")
    return res


@app.route("/logout")
def logout():

    res = make_response(f"<h1> больше не авторизированы</h1>")
    res.set_cookie("logged", "", 0)
    return res


if __name__ == "__main__":
    app.run(debug=True)