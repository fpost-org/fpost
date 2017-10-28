from flask import Flask, request, redirect
from flask.templating import render_template
from app.DB import DB
from app.core import *

DEBUG = False

app = Flask(__name__)
flask_db = DB()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    elif request.method == 'POST':
        return post_processing(request, flask_db)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html')
 
@app.route('/<postname>', methods=['GET'])
def show_post(postname):
    res = DB.getpostbyname(flask_db, postname)
    return render_template('post.html', res=res).replace("!!!Post!!!", res[2])
    
@app.errorhandler(404)
def page_not_found(error):
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = DEBUG)

