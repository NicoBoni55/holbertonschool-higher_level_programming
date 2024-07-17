#!/usr/bin/python3

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", titulo="Welcome to my app :)")

@app.route('/about')
def about():
    return render_template("about.html", titulo="About us")

@app.route('/contact')
def contact():
    return render_template("contact.html", titulo="Contact")

if __name__ == '__main__':
    app.run