#!venv/bin/python3
import random
#import flask
import os
from flask_sqlalchemy import  SQLAlchemy
from config import Config
import shutil
import sqlite3
#from flask import Session
from flask import Flask, g, request, render_template, request, redirect, make_response, session, url_for, flash
app = Flask(__name__)
app.secret_key = b'TOKEN SECRET KEY'
app.config.from_object(Config)
db = SQLAlchemy(app)
def create_db():
    return sqlite3.connect('./db.sqlite')
@app.before_request
def befor_request_hook():
    g.db = create_db()
    g.cur = g.db.cursor()
    print('1. before')
@app.after_request
def after_request_hok(response):
    g.db.close()
    return response
"""
@app.route('/visits-counter/')
def visits():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # reading and updating session data
    else:
        session['visits'] = 1 # setting session data
    return "Total visits: {}".format(session.get('visits'))
 
@app.route('/delete-visits/')
def delete_visits():
    session.pop('visits', None) # delete visits
    return 'Visits deleted'
"""
@app.route('/')
def index():
    return render_template('index.html')
    """
    action = request.args.get('action')
    username = request.args.get('username')
    passwords = request.args.get('password')
    if action and username and passwords:
        if action.lower() == 'register':
            g.cur.execute("INSERT INTO users (username,passwords,Email,name,number,lastname) VALUES (?, ?, ?, ?, ?, ?)", (username,passwords,mail,name,number,lastname))
            g.db.commit()
            return 'user added'
        if action.lower() == 'login':
            g.cur.execute(
                          'select * FROM users WHERE username = ? AND passwords = ?',
                          (username, passwords))
            user = g.cur.fetchone()
            if not user:
                return 'invalid username or password'
            return f'Welcome dear {user[1]}'
    return "hello world"
    """
@app.route("/posts/")
def posts():
    if not session['username']:
        return " برای دیدن پست ها اول ثبت نام کنید <br> <a href='/sign'>ثبت نام</a>"
    #else:
        #return 'hello'
    return render_template("posts.html")
@app.route('/sign',methods=['POST','GET'])
def sign():
    return render_template('sign.html')
@app.route('/sign/signin',methods=['POST','GET'])
def signin():
    user = request.form['username']
    name = request.form['name']
    lastname = request.form['lastname']
    mail = request.form['email']
    number = request.form['number']
    passwords = request.form['pass']
    session['username'] = user
    session['name'] = name
    session['lastname'] = lastname
    session['mail'] = mail
    session['number'] = number
    session['password'] = passwords
    try:
        g.cur.execute("INSERT INTO users (username,passwords,Email,name,number,lastname) VALUES (?, ?, ?, ?, ?, ?)", (user,passwords,mail,name,number,lastname))
        g.db.commit()
        return session["user"]
    except sqlite3.IntegrityError:
        return 'username selected'
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/login',methods=['POST','GET'])
def login():
    return render_template('login.html')
@app.route('/login/login',methods=['POST','GET'])
def log():
    username = request.form['first']
    passwords = request.form['second']
    if username and passwords:
            #g.cur.execute("INSERT INTO users (username,passwords) VALUES (?, ?)", (username,passwords))
            #g.db.commit()
            #return 'user added'
            g.cur.execute(
                          'select * FROM users WHERE username = ? AND passwords = ?',
                          (username, passwords))
            user = g.cur.fetchone()
            if not user:
                return 'invalid username or password'
            return f'Welcome dear {user[1]} with password {user[2]}!' 
@app.route("/search/")
def search():
    return render_template("search.html")
if __name__ == "__main__":
    app.run(debug=True)



"""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(32) NOT NULL UNIQUE,
    passwords VARCHAR(128) NOT NULL 
)
"""
