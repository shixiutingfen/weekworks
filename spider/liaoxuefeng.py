# -*- coding: utf-8 -*-
import  requests
from bs4 import BeautifulSoup
import time
import sys
import MySQLdb
reload(sys)
sys.setdefaultencoding( "utf-8" )
urls = []
r = requests.get(url='https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000', timeout=2.00)
r.encoding = 'utf8'
html = r.text
soup = BeautifulSoup(html, 'html.parser')
divs = soup.findAll(class_='uk-nav-side')
conn=MySQLdb.connect(host='119.29.214.134',user='root',passwd='manjie410',db='tectlean',port=3306,charset='utf8')
cur=conn.cursor()
for i,div in enumerate(divs):
    if i == 1:
        lis = div.findAll('li')
        for li in lis:
            href = li.find('a').get('href')
            text = li.find('a').text
            # print li
            if str(li).find('margin-left:1em;') >0:
                print 'parent'
                strsql = "insert into tec_title(title, title_url, level) values (  '" + text + "', '" + href + " ',1 )"
                cur.execute(strsql)
                conn.commit()
            else:
                timestamp = int(time.time())
                print timestamp;
                title_id = timestamp
                strsql = "select id from tec_title where id = (SELECT max(id) FROM tec_title WHERE  LEVEL =1)"
                #str = "SELECT max(id) FROM tec_title WHERE LEVEL =1"
                cur.execute(strsql)
                conn.commit()
                row = cur.fetchone()
                if row == None:
                    print "empty"
                else:
                    title_id = row[0]
                    if title_id !=1:
                        strsql = "insert into tec_title(title, title_url, level,parentid) values  ( '" + text + "', '" + href + " ',2 ,'"+str(title_id)+"')"
                        cur.execute(strsql)
                        conn.commit()
                        print title_id


