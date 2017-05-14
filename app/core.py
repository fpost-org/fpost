from cgi import escape
import html
import json
import urllib.request
import re
from app.DB import DB

def post_processing(request):
    title = html.unescape(request.form['title'])
    name = html.unescape(request.form['name'])
        
    title = re.sub(r'\<[^>]*\>', '', title)
    name = re.sub(r'\<[^>]*\>', '', name)
        
    json_p = json.loads( html.unescape(request.form['post']) )
    post = ''
    for p in json_p:
        if json_p[p]['type'] == "text":
            cont = urllib.request.unquote(json_p[p]['content'])
            cont = re.sub(r'\<[^>]*\>', '', cont)
            post += '<p>' + cont + '</p>' 
        elif json_p[p]['type'] == "youtube":
            post += '<p>' + urllib.request.unquote(json_p[p]['content']) + '</p>' 
    res = DB().insert_db(title, name, post)
    return '/' + title
    