# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from myapp import app
import json
from flask import render_template, url_for, redirect, request, flash, session, g, abort
from flask import  jsonify
import json
import MySQLdb
import movie_db


@app.route('/index')
def index():
    return render_template("techlearn/index_tech.html",title = 'Home')

@app.route('/index_javscript')
def index_javscript():
    return render_template("techlearn/index_javascript.html",title = 'index_javscript')
@app.route('/index_git')
def index_git():
    return render_template("techlearn/index_git.html",title = 'index_git')
@app.route('/index_linux')
def index_linux():
    return render_template("techlearn/index_linux.html",title = 'index_linux')
@app.route('/usermanage', methods=['GET','POST'])
def usermanage():
    return render_template("usermanage.html",title = 'Home',action='/usermanage')

@app.route('/java_resources', methods=['GET','POST'])
def java_resources():
    return render_template("techlearn/java_resources.html",title = 'Home',action='/java_resources')







