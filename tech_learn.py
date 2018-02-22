# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from myapp import app
from utils import param_util,redis_utils
from flask import render_template, url_for, redirect, request
from flask import  jsonify
import json,os,sys
import MySQLdb
from urllib import unquote

conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='test123',db='dayfilm',port=3306,charset='utf8')
cur=conn.cursor()
@app.route('/getJson')
def get_json():
    requestStr = request.query_string
    params = param_util.getparam(unquote(requestStr))
    type = int(params['type'])
    all_the_text = get_title_type(type)
    return json.dumps(all_the_text)

@app.route('/getContent', methods=['GET','POST'])
def get_content():
    requestStr = request.query_string
    all_the_text = get_content_type(requestStr)
    return jsonify(data=all_the_text)

@app.route('/getSearchJson', methods=['GET','POST'])
def get_search_json():
    requestStr = request.query_string
    params = param_util.getparam(unquote(requestStr))
    type = int(params['type'])
    all_the_text = get_search_json(type)
    return jsonify(data=all_the_text)

@app.route('/getFirstPage', methods=['GET','POST'])
def get_first_page():
    requestStr = request.query_string
    params = param_util.getparam(unquote(requestStr))
    type = int(params['type'])
    all_the_text = get_first_type(type)
    return jsonify(data=all_the_text)

def get_title_type(type):
    if 1 == type:
        fname =  os.path.abspath(os.path.dirname(__file__))+'/content/module/liaoxuefeng_python.txt'
    elif 2== type:
        fname =  os.path.abspath(os.path.dirname(__file__))+'/content/module/liaoxuefeng_javascript.txt'
    elif 3 == type:
        fname =  os.path.abspath(os.path.dirname(__file__))+'/content/module/liaoxuefeng_git.txt'
    elif 4 == type:
        fname =  os.path.abspath(os.path.dirname(__file__))+'/content/module/linux_order.txt'
    fobj=open(fname)
    try:
        all_the_text = fobj.read()
    except IOError:
        print '*** file open error:'
    finally:
        fobj.close()
    return all_the_text

def get_search_json(type):
    if 1 == type:
        fname =  os.path.abspath(os.path.dirname(__file__))+'/content/module/search/linux_order.txt'
    elif 2== type:
        fname =  os.path.abspath(os.path.dirname(__file__))+'/content/module/liaoxuefeng_javascript.txt'
    elif 3 == type:
        fname =  os.path.abspath(os.path.dirname(__file__))+'/content/module/liaoxuefeng_git.txt'
    elif 4 == type:
        fname =  os.path.abspath(os.path.dirname(__file__))+'/content/module/search/linux_order.txt'
    fobj=open(fname)
    try:
        all_the_text = fobj.read()
    except IOError:
        print '*** file open error:'
    finally:
        fobj.close()
    return all_the_text

def get_content_type(requestStr):
    params = param_util.getparam(unquote(requestStr))
    url = params['url']
    type = int(params['type'])
    base_dir = ''
    if 1 == type:#python
        base_dir = os.path.abspath(os.path.dirname(__file__))+'/content/python/liaoxuefeng/'
    elif 2 == type:#javascript
        base_dir = os.path.abspath(os.path.dirname(__file__))+'/content/javascript/liaoxuefeng/'
    elif 3 == type:#git
        base_dir = os.path.abspath(os.path.dirname(__file__))+'/content/git/liaoxuefeng/'
    elif 4 == type:
        base_dir = os.path.abspath(os.path.dirname(__file__))+'/content/linux/order/'
    fname = base_dir + str(url[0:len(url)-1])
    fobj = open(fname)
    try:
        all_the_text = fobj.read()
    except IOError:
        print '*** file open error:'
    finally:
        fobj.close()
    return all_the_text

def get_first_type(type):
    base_dir = ''
    if 1 == type:#python
        base_dir = os.path.abspath(os.path.dirname(__file__))+'/content/python/liaoxuefeng/'
        url = '145ab030-b01c-11e7-a8a0-aced5cefb22f.txt' #Python简介
    elif 2 == type:#javascript
        base_dir = os.path.abspath(os.path.dirname(__file__))+'/content/javascript/liaoxuefeng/'
        url = 'a35c7a4f-b34d-11e7-ab18-aced5cefb22f.txt' #基本语法
    elif 3 == type:#git
        base_dir = os.path.abspath(os.path.dirname(__file__))+'/content/git/liaoxuefeng/'
        url = '73c7ec0f-b5a6-11e7-8a79-aced5cefb22f.txt'#Git简介
    elif 4 == type:#git
        base_dir = os.path.abspath(os.path.dirname(__file__))+'/content/linux/order/'
        url = '4525ee1e-c0a5-11e7-8c43-aced5cefb22f.txt'#Git简介
    fname = base_dir + str(url[0:len(url)])
    fobj = open(fname)
    try:
        all_the_text = fobj.read()
    except IOError:
        print '*** file open error:'
    finally:
        fobj.close()
    return all_the_text