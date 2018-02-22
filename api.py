# -*- coding: utf-8 -*-
from flask import Flask,jsonify,request
from myapp import app
import MySQLdb,time

conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='test123',db='dayfilm',port=3306,charset='utf8')
cur=conn.cursor()

@app.route('/api/getdata',methods=['GET'])
def get_tasks():
    return jsonify({'data':'aa'})

@app.route('/api/getPageData',methods=['POST'])
def getPageData():
    pageNum = request.json['params']['page']
    pageSize = request.json['params']['pageSize']
    start = (int(pageNum)-1)*int(pageSize)
    cur.execute("select id,title,title_type from tec_title  limit "+str(start)+","+str(pageSize))
    results = cur.fetchall()
    cur.execute("select count(1) from tec_title  ")
    totalCount  = cur.fetchone()
    data = []
    for result in results:
        id=  result[0]
        name = result[1]
        type = result[2]
        data.append({'id':id,'name':name,'type':type})
    return jsonify({'data':data,'totalCount':totalCount[0]})

@app.route('/api/insertdata',methods=['POST'])
def insertdata():
    timestamp = int(time.time())
    title_id = timestamp
    name = request.json['params']['name']
    sqlstr = "insert into tec_title  (id,title,title_type) values ("+str(title_id)+",'"+str(name)+"',3)"
    print sqlstr
    cur.execute(sqlstr)
    conn.commit()
    return jsonify({'msg':'0'})

@app.route('/api/deletedata',methods=['POST'])
def deletedata():
    id = request.json['params']['id']
    sqlstr = "delete from tec_title WHERE  id="+str(id)
    cur.execute(sqlstr)
    conn.commit()
    return jsonify({'msg':'0'})