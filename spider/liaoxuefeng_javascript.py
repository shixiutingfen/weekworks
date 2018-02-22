# -*- coding: utf-8 -*-
import  requests
from bs4 import BeautifulSoup
import time,uuid
import sys
import MySQLdb
reload(sys)
sys.setdefaultencoding( "utf-8" )
conn=MySQLdb.connect(host='119.29.214.134',user='root',passwd='manjie410',db='tectlean',port=3306,charset='utf8')
cur=conn.cursor()
urls = []
r = requests.get(url='https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000', timeout=2.00)
r.encoding = 'utf8'
html = r.text
soup = BeautifulSoup(html, 'html.parser')
divs = soup.findAll("div", attrs={"depth": "1"})

for i,div in enumerate(divs):
    print div
    a1id =  uuid.uuid1()
    a1 = div.find('a').get('href')
    a1text = div.find('a').text
    print a1id
    strsql1 = "insert into tec_title(id,title, title_url, level,title_type) values (  '"+str(a1id)+"','" + a1text + "', '" + a1 + " ',1,3 )"
    cur.execute(strsql1)
    conn.commit()
    divs2 = div.findAll("div", attrs={"depth": "2"})
    for j,div2 in enumerate(divs2):
        a2id =  uuid.uuid1()
        print a2id
        a2 = div2.find('a').get('href')
        a2text = div2.find('a').text
        strsql2 = "insert into tec_title(id,title, title_url, level,parentid,title_type) values  ( '"+str(a2id)+"','" + a2text + "', '" + a2 + " ',2 ,'"+str(a1id)+"',3)"
        cur.execute(strsql2)
        conn.commit()
        divs3 = div2.findAll("div", attrs={"depth": "3"})
        for k,div3 in enumerate(divs3):
            a3id =  uuid.uuid1()
            print a3id
            a3 = div3.find('a').get('href')
            a3text = div3.find('a').text
            strsql2 = "insert into tec_title(id,title, title_url, level,parentid,title_type) values  ( '"+str(a3id)+"','" + a3text + "', '" + a3 + " ',3 ,'"+str(a2id)+"',3)"
            cur.execute(strsql2)
            conn.commit()
            divs4 = div3.findAll("div", attrs={"depth": "4"})
            for p,div4 in enumerate(divs4):
                a4id =  uuid.uuid1()
                print a4id
                a4 = div4.find('a').get('href')
                a4text = div4.find('a').text
                strsql2 = "insert into tec_title(id,title, title_url, level,parentid,title_type) values  ( '"+str(a4id)+"','" + a4text + "', '" + a4 + " ',4 ,'"+str(a3id)+"',3)"
                cur.execute(strsql2)
                conn.commit()


