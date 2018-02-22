# -*- coding: utf-8 -*-

##获取最新电影
def getLatestFilm():
    brief  = db.session.execute(sql_constant.QUERY_LATEST_FILM)
    latestFilmList = []
    for i in brief:
        filmdict = {'title': i.title[0:17],'id':i.id}
        latestFilmList.append(filmdict)
    return latestFilmList
