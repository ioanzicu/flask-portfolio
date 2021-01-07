import os
from flask import Flask, render_template
from flask.helpers import send_from_directory
app = Flask(__name__)
print(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)
