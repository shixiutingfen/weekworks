# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import uuid
from myapp import app
from utils import param_util,redis_utils
from flask import render_template, url_for, redirect, request
from flask import  jsonify
import json,os,sys
import MySQLdb
from urllib import unquote

conn=MySQLdb.connect(host='119.29.214.134',user='root',passwd='manjie410',db='tectlean',port=3306,charset='utf8')
cur=conn.cursor()
strsql2 = "SELECT t.parentid FROM tec_title t WHERE t.level=2 AND t.title_type=4 GROUP BY t.parentid "
cur.execute(strsql2)
conn.commit()
rows = cur.fetchall()
childmap = {}
for row in rows:
    strsql3 = "select t.id ,t.title ,c.content  from tec_title t LEFT  join tec_content c on t.id = c.titleid where t.title_type = 4 AND t.parentid='"+str(row[0])+"'"
    cur.execute(strsql3)
    conn.commit()
    children = cur.fetchall()
    childresult = []
    for child in children:
        childresult.append({'id':str(child[0]),'name':child[1],'url':child[2]})
    childmap[str(row[0])] = childresult
strsql = "select t.id ,t.title,c.content  from tec_title t LEFT  join tec_content c on t.id = c.titleid  where t.title_type = 4 AND t.level=1"
cur.execute(strsql)
conn.commit()
nones=[]
rows = cur.fetchall()
for row in rows:
    if str(row[0]) in childmap:
        nones.append({'id':row[0],'name':row[1],'spread':'true','url':row[2],'children':childmap[str(row[0])]})
    else:
         nones.append({'id':row[0],'name':row[1],'spread':'true','url':row[2]})
#python_nodes = redis_utils.get_key('python')
res_data=json.dumps(nones,ensure_ascii=False,encoding="gb2312")
print res_data