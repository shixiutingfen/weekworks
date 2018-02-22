# -*- coding: utf-8 -*-
import  requests
from bs4 import BeautifulSoup
import re
import sys
import MySQLdb
reload(sys)
sys.setdefaultencoding( "utf-8" )
urls = []
r = requests.get(url='http://www.autohome.com.cn/qk/', timeout=2.00)
r.encoding = 'GBK'
html = r.text
#print html
soup = BeautifulSoup(html, 'html.parser')
#divs = soup.findAll("div", {"id" : re.compile('divCsLevel_*')})
#divs = soup.findAll("div", {"id" : 'divCsLevel_1'})
#f = open('D:\\carkind\\qingke.txt', 'r+')
divs = soup.findAll(class_='tab-content-item')
conn=MySQLdb.connect(host='192.168.0.159',user='root',passwd='Ast4HS',db='u2s',port=3306,charset='utf8')
cur=conn.cursor()
for i,div in enumerate(divs):
    if i == 0:
        uiboxes = div.findAll(class_='uibox')
        for uibox in uiboxes:
            dls = uibox.findAll('dl')

            for dl in dls:
                dd = dl.find('dd')
                #linestr = ''
                brandname = dd.find(class_='h3-tit').text
                #linestr+=brandname+","
                #print brandname+"-------------------------------"
                bigbrandname = dl.find('dt').find('div').find('a').text
                print bigbrandname
                serieses = dl.find('dd').findAll('li')
                for series in serieses:
                    try:
                        series_name=series.find('h4').find('a').text
                        strsql = "insert into carkind_jiuling(brand_name, car_series_name,bigbrandname, carkindname) values ('" + brandname + "','" + series_name+ "','" + bigbrandname + "','轻客')"
                        cur.execute(strsql)
                        conn.commit()
                        #linestr+=series_name+","
                    except :
                         continue
                #print linestr
                #f.write(linestr+'\n')
       # print line
#f.close()

#

