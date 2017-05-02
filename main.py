from flask import Flask, request, redirect
from flask.templating import render_template
import sqlite3
from app.DB import DB
from app.post import Content

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    elif request.method == 'POST':
        return render_template('index.html')
    
@app.errorhandler(404)
def page_not_found(error):
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)