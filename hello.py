import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<img src="http://t1.gstatic.com/images?q=tbn:ANd9GcRMMh5MUMdgPHTFYS-RfCBzgmnRV5liQhKc1QScmt830x8UUMk00g"></img>'
