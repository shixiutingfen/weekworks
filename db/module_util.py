# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import MySQLdb,json
conn=MySQLdb.connect(host='119.29.214.134',user='root',passwd='manjie410',db='tectlean',port=3306,charset='utf8')
cur=conn.cursor()
leve4_parentid =  ['8c83e530-b34c-11e7-b6ca-aced5cefb22f','8cac54c0-b34c-11e7-ba53-aced5cefb22f','8cc4bec0-b34c-11e7-a675-aced5cefb22f','8cf03b91-b34c-11e7-aae4-aced5cefb22f','8d36e180-b34c-11e7-8da1-aced5cefb22f','8f477200-b34c-11e7-9e61-aced5cefb22f']
leve3_parentid = ['807495a1-b34c-11e7-aed5-aced5cefb22f','82f8a870-b34c-11e7-9a47-aced5cefb22f','84920d21-b34c-11e7-a8b5-aced5cefb22f','84e906c0-b34c-11e7-987f-aced5cefb22f','89c9801e-b34c-11e7-bdf9-aced5cefb22f','8c76c5d1-b34c-11e7-900a-aced5cefb22f']
leve2_parentid =  ['7dd5cede-b34c-11e7-87dd-aced5cefb22f','80585b11-b34c-11e7-8988-aced5cefb22f','80ad58e1-b34c-11e7-a961-aced5cefb22f','81a155cf-b34c-11e7-9382-aced5cefb22f','824c89f0-b34c-11e7-a7c8-aced5cefb22f','844ee9a1-b34c-11e7-a88c-aced5cefb22f','86059a4f-b34c-11e7-a43b-aced5cefb22f','86ec50d1-b34c-11e7-9763-aced5cefb22f','88c35ac0-b34c-11e7-8b0a-aced5cefb22f']

childmap4 = {}
for parentid4 in leve4_parentid:
     strsql4 = "select t.id ,t.title ,c.content  from tec_title t LEFT  join tec_content c on t.id = c.titleid where t.title_type = 2 AND t.parentid='"+str(parentid4)+"'"
     cur.execute(strsql4)
     conn.commit()
     children4 = cur.fetchall()
     childresult4 = []
     for child in children4:
         childresult4.append({'id':str(child[0]),'name':child[1],'url':child[2]})
         childmap4[str(parentid4)] = childresult4
res_data1=json.dumps(childmap4,ensure_ascii=False,encoding="gb2312")
#print res_data1
childmap3 = {}
for parentid3 in leve3_parentid:
     strsql3 = "select t.id ,t.title ,c.content  from tec_title t LEFT  join tec_content c on t.id = c.titleid where t.title_type = 2 AND t.parentid='"+str(parentid3)+"'"
     cur.execute(strsql3)
     conn.commit()
     children3 = cur.fetchall()
     childresult3 = []
     for child3 in children3:
         childresult3.append({'id':str(child3[0]),'name':child3[1],'url':child3[2]})
         childmap3[str(parentid3)] = childresult3
res_data2=json.dumps(childmap3,ensure_ascii=False,encoding="gb2312")
#print res_data2
childmap2 = {}
for parentid2 in leve2_parentid:
     strsql2 = "select t.id ,t.title ,c.content  from tec_title t LEFT  join tec_content c on t.id = c.titleid where t.title_type = 2 AND t.parentid='"+str(parentid2)+"'"
     cur.execute(strsql2)
     conn.commit()
     children2 = cur.fetchall()
     childresult2 = []
     for child2 in children2:
         childresult2.append({'id':str(child2[0]),'name':child2[1],'url':child2[2]})
         childmap2[str(parentid2)] = childresult2
res_data=json.dumps(childmap2,ensure_ascii=False,encoding="gb2312")
#print res_data
cur.execute("SELECT t.id,t.title,t.parentid,t.level FROM tec_title t where t.title_type=2 AND t.level=1")
results = cur.fetchall()
nones=[]
for result in results:
    if str(result[0]) in childmap2:
        nones.append({'id':result[0],'name':result[1],'spread':'true','url':result[2],'children':childmap2[str(result[0])]})
    else:
        nones.append({'id':result[0],'name':result[1],'spread':'true','url':result[2]})
res_data=json.dumps(nones,ensure_ascii=False,encoding="gb2312")
print res_data

 # strsql2 = "SELECT t.parentid FROM tec_title t WHERE t.level=2 GROUP BY t.parentid "
    # cur.execute(strsql2)
    # conn.commit()
    # rows = cur.fetchall()
    # childmap = {}
    # for row in rows:
    #     strsql3 = "select t.id ,t.title ,c.content  from tec_title t LEFT  join tec_content c on t.id = c.titleid where t.title_type = 1 AND t.parentid="+str(row[0])
    #     cur.execute(strsql3)
    #     conn.commit()
    #     children = cur.fetchall()
    #     childresult = []
    #     for child in children:
    #         childresult.append({'id':str(child[0]),'name':child[1],'url':child[2]})
    #     childmap[str(row[0])] = childresult
    # strsql = "select t.id ,t.title,c.content  from tec_title t LEFT  join tec_content c on t.id = c.titleid  where t.title_type = 1 AND t.level=1"
    # cur.execute(strsql)
    # conn.commit()
    # nones=[]
    # rows = cur.fetchall()
    # for row in rows:
    #     if str(row[0]) in childmap:
    #         nones.append({'id':row[0],'name':row[1],'spread':'true','url':row[2],'children':childmap[str(row[0])]})
    #     else:
    #          nones.append({'id':row[0],'name':row[1],'spread':'true','url':row[2]})
    # #python_nodes = redis_utils.get_key('python')
    # res_data=json.dumps(nones,ensure_ascii=False,encoding="gb2312")
    # print res_data
    # redis_utils.set_key("shixiuting",res_data)