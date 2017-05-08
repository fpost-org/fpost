from flask import Flask, request, redirect
from flask.templating import render_template
from app.DB import DB
from app.post import Content
from cgi import escape
import html

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    elif request.method == 'POST':
        title = html.unescape(request.form['title'])
        name = html.unescape(request.form['name'])
        post = ""
        for param in request.form:
            key = format(param);
            if key.find("post") == 0:
                post = post + "<p>" + request.form.get(key) + "</p>"
        post = html.unescape(post);
        res = DB().insert_db(title, name, post)
        return '/' + title

@app.route('/db', methods=['GET'])
def show_db():
    return DB().show_db()

@app.route('/create', methods=['GET'])
def create_db():
    return DB().create_db()
 
@app.route('/<postname>', methods=['GET'])
def show_post(postname):
    res = DB().getpostbyname(postname)
    return render_template('post.html', res=res).replace("!!!Post!!!", res[2])
    
@app.errorhandler(404)
def page_not_found(error):
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=False)