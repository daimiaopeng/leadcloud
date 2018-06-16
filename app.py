# coding: utf-8

from datetime import datetime

from flask import *
from flask import render_template
from flask_sockets import Sockets
from 爬IT_HOME import *
import re
import leancloud


app = Flask(__name__)
sockets = Sockets(app)

@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['text']
        Url = leancloud.Object.extend('it_url')
        comment = Url()
        query = comment.get('comment')
        comment.set('url', str(url))
        comment.save()
        num = re.search('\d{1,7}', url).group(0)
        list = getpage_commentinfo(str(num))
        # print(num)
        print(url)
        return render_template('index.html',list=list)
    if request.method == 'GET':
        return render_template('index.html')





@sockets.route('/echo')
def echo_socket(ws):
    while True:
        message = ws.receive()
        ws.send(message)
