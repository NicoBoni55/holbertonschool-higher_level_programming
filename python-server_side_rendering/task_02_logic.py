#!/usr/bin/python3

from flask import Flask, render_template
import json


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

@app.route('/items')
def item_list():
    with open("items.json", "r") as json_file:
        items_json = json.load(json_file)
        
        items = items_json.get('items')
    return render_template("items.html", titulo="Items List", items=items)
if __name__ == '__main__':
    app.run(debug=True)