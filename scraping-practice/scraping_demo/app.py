from flask import Flask, render_template
from data_generator import generate_article, generate_products, generate_reviews
from faker import Faker

import random



app = Flask(__name__)
fake = Faker("ja_JP")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/products')
def products():
    items = generate_products()
    return render_template("products.html", items=items)

@app.route('/article')
def article():
    data = generate_article()
    return render_template("article.html", **data)

@app.route('/reviews')
def reviews():
    reviews = generate_reviews()
    return render_template("reviews.html", reviews=reviews)