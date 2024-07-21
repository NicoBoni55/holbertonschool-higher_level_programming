#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv
import sqlite3

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
    if source not in ['json', 'csv', 'sql']:
        return render_template("product_display.html", error="Wrong source"), 400
    
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

        elif source == 'sql':
            conn = sqlite3.connect('products.db')
            cursor = conn.cursor()
    
            query = 'SELECT * FROM Products'
            params = ()
    
            if product_id:
                query += ' WHERE id = ?'
                params = (int(product_id),)
    
            cursor.execute(query, params)
            rows = cursor.fetchall()

            conn.close()

            columns = ['id', 'name', 'category', 'price']

            product_list = []
            for row in rows:
                product_dict = {}
                for key, value in zip(columns, row):
                    product_dict[key] = value
                product_list.append(product_dict)


    except FileNotFoundError:
        return render_template("product_display.html", error="File not found"), 404

    if product_id:
        try:
            product_id = int(product_id)
        except:
            return render_template("product_display.html", error="Product not found"), 400
        filtered_products = []
        for product in product_list:
            if product['id'] == product_id:
                filtered_products.append(product)

        product_list = filtered_products


    return render_template("product_display.html", titulo="Product table", Products=product_list)
    
if __name__ == '__main__':
    app.run(debug=True)