#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv
import os


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

@app.route('/products')
def table_products():

    source = request.args.get('source')
    product_id = request.args.get('id')
    
    if not source:
        return render_template("product_display.html", error="Source parameter is required"), 400
    if source not in ['json', 'csv']:
        return render_template("product_display.html", error="Wrong source"), 200
    
    product_list = []
    
    try:
        if source == 'json':
            with open('products.json', 'r') as json_file:
                product_list = json.load(json_file)

        elif source == 'csv':
            with open('products.csv', 'r') as csv_file:
                data_csv = csv.DictReader(csv_file)
                for product in data_csv:
                    if 'id' in product:
                        product['id'] = int(product['id'])
                    product_list.append(product)

    except FileNotFoundError:
        return render_template("product_display.html", error="File not found"), 404

    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template("product_display.html", error="Product ID not valid"), 200
        filtered_products = []
        for product in product_list:
            if product['id'] == product_id:
                filtered_products.append(product)
            if not filtered_products:
                return render_template("product_display.html", error="Product not found."), 404

        product_list = filtered_products


    return render_template("product_display.html", titulo="Product table", Products=product_list)
    
if __name__ == '__main__':
    app.run(debug=True)