from flask import Flask, request, redirect, send_from_directory
from flask.templating import render_template
from app.DB import DB
from app.core import *
import os

DEBUG = False
app = Flask(__name__)
flask_db = DB()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    elif request.method == 'POST':
        return post_processing(request, flask_db)

@app.route('/favicon.ico')
def icon():
    return send_from_directory(os.path.join(app.root_path, 'static', 'img'), 'favicon.ico',  mimetype='image/png')

@app.route('/<postname>', methods=['GET'])
def show_post(postname):
    res = flask_db.getpostbyname(postname)
    return render_template('post.html', res=res).replace('<div class="post"></div>', '<div class="post">'+res[2]+'</div>' )
    
@app.errorhandler(404)
def page_not_found(error):
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = DEBUG)

