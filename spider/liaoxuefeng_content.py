# -*- coding: utf-8 -*-
import  requests
from bs4 import BeautifulSoup
import time
import uuid
import sys
import MySQLdb
reload(sys)
sys.setdefaultencoding( "utf-8" )
urls = []
base_url = 'https://www.liaoxuefeng.com'
# r = requests.get(url='https://www.liaoxuefeng.com/', timeout=2.00)
# r.encoding = 'utf8'
# html = r.text
#soup = BeautifulSoup(html, 'html.parser')
conn=MySQLdb.connect(host='119.29.214.134',user='root',passwd='manjie410',db='tectlean',port=3306,charset='utf8')
cur=conn.cursor()
base_dir = 'D:/svn/tecent/weekworks/content/python/liaoxuefeng/'
cur.execute("select id,title_url from tec_title")
results = cur.fetchall()
for row in results:
    print row[0]
    url = base_url + row[1]
    req = requests.get(url=url, timeout=2.00)
    req.encoding = 'utf8'
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find(class_='x-content')
    filename = str(uuid.uuid1())+'.txt'
    fname = base_dir+filename
    print fname
    try:
        fobj=open(fname,'a')                 # 这里的a意思是追加，这样在加了之后就不会覆盖掉源文件中的内容，如果是w则会覆盖。
    except IOError:
        print '*** file open error:'
    else:
        fobj.write(str(content))   #  这里的\n的意思是在源文件末尾换行，即新加内容另起一行插入。
        strsql = "insert into tec_content(titleid, content) values (  '" + str(row[0]) + "', '" + str(filename) + " ' )"
        cur.execute(strsql)
        conn.commit()
        fobj.close()
    # strsql = "insert into tec_content(titleid, content) values  ( '" + str(row[0]) + "', '" + str(content) + "')"
    # print strsql
    # cur.execute(strsql)
    # conn.commit()
    #print divs
# for i,div in enumerate(divs):
#     if i == 1:
#         lis = div.findAll('li')
#         for li in lis:
#             href = li.find('a').get('href')
#             text = li.find('a').text
#             # print li
#             if str(li).find('margin-left:1em;') >0:
#                 print 'parent'
#                 strsql = "insert into tec_title(title, title_url, level) values (  '" + text + "', '" + href + " ',1 )"
#                 cur.execute(strsql)
#                 conn.commit()
#             else:
#                 timestamp = int(time.time())
#                 print timestamp;
#                 title_id = timestamp
#                 strsql = "select id from tec_title where id = (SELECT max(id) FROM tec_title WHERE  LEVEL =1)"
#                 #str = "SELECT max(id) FROM tec_title WHERE LEVEL =1"
#                 cur.execute(strsql)
#                 conn.commit()
#                 row = cur.fetchone()
#                 if row == None:
#                     print "empty"
#                 else:
#                     title_id = row[0]
#                     if title_id !=1:
#                         strsql = "insert into tec_title(title, title_url, level,parentid) values  ( '" + text + "', '" + href + " ',2 ,'"+str(title_id)+"')"
#                         cur.execute(strsql)
#                         conn.commit()
#                         print title_id


