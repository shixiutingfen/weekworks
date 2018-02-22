# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import hashlib
"""
	获取链接传参 如a=111&b=222
	最后转化为{'a': '111', 'b': '222'}
"""
def getparam(str):
	params=str.split("&")
	l1=[]
	l2=[]
	for param in params:
		l1.append(param.split("=")[0])
		l2.append(param.split("=")[1])
	resultmap=dict(zip(l1,l2))
	return resultmap

"""
转化ajax的ids
"""
def getAjaxIds(str):
	params=str.split("&")
	l1=[]
	for param in params:
		l1.append(param.split("=")[1])
	return l1


"""
截取文章字符
"""
def getArticleStr(str):
	params=str.split("&")
	l1=[]
	l1.append(str[str.index("title=")+6:str.index("catagoryid=")-1])
	l1.append(str[str.index("catagoryid=")+11:str.index("content=")-1])
	l1.append(str[str.index("content=")+8:len(str)])
	return l1


"""
	md5密码加密
"""
def getenctry(password):
	m = hashlib.md5()
	m.update(password) 
	return m.hexdigest()

if __name__ == '__main__':
	#password=getenctry("123")
	param=getparam("a=111&b=222")
	print param