#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 13:43:01 2016

@author: meemee
"""

import pymongo
from eventregistry import *
import datetime

asx = ['AMP', 'ANZ', 'BHP', 'CBA', 'IAG', 'MQG', 'NAB', 'QBE', 'RIO', 'SUN', 'TCL', 'TLS', 'WBC', 'WFD', 'WOW']
client = pymongo.MongoClient('mongodb://admin1:admin1@ds059306.mlab.com:59306/heroku_ph242ktw')
db = client.get_default_database()
newsdb = db['news_rec']




now = datetime.datetime.now()
past = now - datetime.timedelta(days = 11)
start = past.strftime("%Y-%m-%d")
end = now.strftime("%Y-%m-%d")

ssplit = start.split("-")
s_y = int(ssplit[0])
s_m = int(ssplit[1])
s_d = int(ssplit[2])

esplit = start.split("-")
e_y = int(ssplit[0])
e_m = int(ssplit[1])
e_d = int(ssplit[2])

news = []
er = EventRegistry()
q = QueryArticles()
q.setDateLimit(datetime.date(s_y, s_m, s_d), datetime.date(e_y, e_m, e_d))
#q.addKeyword("iphone")
q.addConcept(er.getConceptUri("australia"))
q.addRequestedResult(RequestArticlesInfo(count = 50,
                                         returnInfo = ReturnInfo(
                                                                 articleInfo = ArticleInfoFlags(duplicateList = False, title = True))))
for item in asx:
    q.addKeyword(item)
    data = er.execQuery(q)
    print(data)
    name = str(item+".AX")
    
    news.append(data)                
    if news != []:
        for item in news:
            new = item.get('articles',{}).get('results', {})
            for article in new:
                if article.get('lang') == ('eng'):
                    date = article.get('date')
                    dsplit = date.split("-")
                    d_y = int(dsplit[0])
                    d_m = int(dsplit[1])
                    d_d = int(dsplit[2])
                    url = article.get('url')
                    title = article.get('title')
                    body = article.get('body')
                    parsart = {
                        "ASX code": name,
                        "Date": datetime.datetime(d_y, d_m, d_d, 0, 0),
                        "URL": str(url),
                        "Title":title,
                        "Body": body
                        }
                        
                    newsdb.insert_one(parsart)
                    print(parsart)