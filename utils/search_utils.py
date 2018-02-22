# -*- coding: utf-8 -*-
import  requests
from bs4 import BeautifulSoup
import uuid,json
import sys
import MySQLdb
reload(sys)
sys.setdefaultencoding( "utf-8" )

conn=MySQLdb.connect(host='119.29.214.134',user='root',passwd='manjie410',db='tectlean',port=3306,charset='utf8')
cur=conn.cursor()
cur.execute("select t.title,c.content FROM tec_title t LEFT JOIN tec_content c ON t.id = c.titleid WHERE t.title_type=3 ")
results = cur.fetchall()
content = []
for row in results:
    title =  row[0]
    url =  row[1]
    content.append({'label':str(title),'value':str(url).decode('UTF-8')})
res_data=json.dumps(content,ensure_ascii=False,encoding="UTF-8")
print res_data
filename = 'D:/svn/tecent/weekworks/content/module/search/git_liaoxuefeng.txt'
try:
    fobj=open(filename,'a')                 # 这里的a意思是追加，这样在加了之后就不会覆盖掉源文件中的内容，如果是w则会覆盖。
except IOError:
    print '*** file open error:'
else:
    fobj.write(str(content))   #  这里的\n的意思是在源文件末尾换行，即新加内容另起一行插入。
    fobj.close()