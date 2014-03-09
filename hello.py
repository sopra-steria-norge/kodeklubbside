import os
from flask import Flask, request, url_for, redirect

app = Flask(__name__, static_url_path='')

@app.route('/')
def hello():
    #return 'Hello World!'
    #return app.send_static_file('index.html')
    return redirect(url_for('static', filename='filen.html'))