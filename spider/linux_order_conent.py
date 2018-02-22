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
base_dir = 'D:/svn/tecent/weekworks/content/linux/order/'
cur.execute("select id,title_url from tec_title WHERE title_type=4 AND  LEVEL =2")
results = cur.fetchall()
for row in results:
    print row[0]
    url =  row[1]
    req = requests.get(url=url)
    req.encoding = 'utf8'
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find(class_='post_bd')
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