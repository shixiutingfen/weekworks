# -*- coding: utf-8 -*-
import  requests
from bs4 import BeautifulSoup
import time,uuid
import sys
import MySQLdb
reload(sys)
sys.setdefaultencoding( "utf-8" )
base_url = 'http://man.linuxde.net/par/'
conn=MySQLdb.connect(host='119.29.214.134',user='root',passwd='manjie410',db='tectlean',port=3306,charset='utf8')
cur=conn.cursor()
for i in range(5):
    url = 'http://man.linuxde.net/par/'+str(i+1)
    r = requests.get(url)
    r.encoding = 'utf-8'
    html = r.text
    a1id =  uuid.uuid1()
    soup = BeautifulSoup(html, 'html.parser')
    bigtitle = soup.find(class_='list_hd').h1.text
    strsql1 = "insert into tec_title(id,title, level,title_type) values (  '"+str(a1id)+"','" + str(bigtitle) + "', 1,4 )"
    cur.execute(strsql1)
    conn.commit()
    print bigtitle
    for j in range(3):
        url2 = url+'/page/'+str(j+1)
        r2 = requests.get(url2)
        print url2
        html2 = r2.text
        soup2 = BeautifulSoup(html2, 'html.parser')
        items = soup2.findAll(class_='item')
        #strsql1 = "insert into tec_title(id,title, title_url, level,title_type) values (  '"+str(a1id)+"','" + a1text + "', '" + a1 + " ',1,3 )"
        for item in items:
            name = item.find('a').text
            href = item.find('a').get('href')
            dec = item.find(class_='des').text
            a2id =  uuid.uuid1()
            strsql2 = "insert into tec_title(id,title, title_url, level,parentid,title_type,c1) values  ( '"+str(a2id)+"','" + name + "', '" + href + " ',2 ,'"+str(a1id)+"',4,'"+str(dec)+"')"
            cur.execute(strsql2)
            conn.commit()
            print name