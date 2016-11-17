#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 13:43:01 2016

@author: meemee
"""

from pymongo import MongoClient
from eventregistry import *
import datetime
import json

asx = ['ABP', 'ACX', 'ABC', 'AGL', 'ALQ', 'ALU', 'AWC', 'AMC', 'AMP', 'ANN', 'APA', 'APN', 'APO', 'ARB', 'AAD', 'ALL', 'AHY', 'ASX', 'AZJ', 'AST', 'ANZ', 'AAC', 'API', 'AHG', 'AOG', 'BOQ', 'BAP', 'BPT', 'BGA', 'BAL', 'BEN', 'BHP', 'BKL', 'BSL', 'BLD', 'BXB', 'BRG', 'BKW', 'BTT', 'BWP', 'CTX', 'CAR', 'CGF', 'CHC', 'CQR', 'CIM', 'CWY', 'CCL', 'COH', 'CBA', 'CPU', 'CTD', 'CGC', 'CCP', 'CMW', 'CWN', 'CSL', 'CSR', 'CYB', 'DXS', 'DMP', 'DOW', 'DUE', 'DLX', 'ECX', 'EHE', 'EVN', 'FXJ', 'FPH', 'FBU', 'FXL', 'FLT', 'FMG', 'GUD', 'GEM', 'GXY', 'GTY', 'GMA', 'GMG', 'GPT', 'GNC', 'GXL', 'GOZ', 'GWA', 'HVN', 'HSO', 'HGG', 'ILU', 'IPL', 'IGO', 'IFN', 'IAG', 'IOF', 'IVC', 'IFL', 'IPH', 'IRE', 'INM', 'ISD', 'JBH', 'A2M', 'JHC', 'JHX', 'LLC', 'LNK', 'MFG', 'MGR', 'MIN', 'MMS', 'MND', 'MPL', 'MQA', 'MQG', 'MTR', 'MTS', 'MYO', 'MYR', 'MYX', 'NAB', 'NCM', 'NEC', 'NSR', 'NST', 'NUF', 'NVT', 'NWS', 'NXT', 'OFX', 'ORA', 'ORE', 'ORG', 'ORI', 'OSH', 'OZL', 'PGH', 'PMV', 'PPT', 'PRY', 'PTM', 'QAN', 'QBE', 'QUB', 'REA', 'REG', 'RFG', 'RHC', 'RIO', 'RMD', 'RRL', 'RSG', 'RWC', 'S32', 'SAI', 'SAR', 'SBM', 'SCG', 'SCP', 'SDF', 'SEK', 'SFR', 'SGM', 'SGP', 'SGR', 'SHL', 'SIP', 'SKC', 'SKI', 'SKT', 'SPK', 'SPO', 'SRX', 'STO', 'SUL', 'SUN', 'SVW', 'SWM', 'SXL', 'SYD', 'SYR', 'TAH', 'TCL', 'TGR', 'TLS', 'TME', 'TNE', 'TPM', 'TTS', 'TWE', 'VCX', 'VOC', 'VRT', 'WBC', 'WEB', 'WES', 'WFD', 'WHC', 'WOR', 'WOW', 'WPL', 'WSA']
client = MongoClient('mongodb://admin1:admin1@ds059306.mlab.com:59306/heroku_ph242ktw')
db = client.get_default_database()
histo = db['news_rec']

now = datetime.datetime.now()
past = now - datetime.timedelta(days = 0)
past2 = past - datetime.timedelta(days = 60)
start = past2.strftime("%Y-%m-%d")
end = past.strftime("%Y-%m-%d")

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
q.addConcept(er.getConceptUri("energy"))
q.addRequestedResult(RequestArticlesInfo(count = 50,
                                         returnInfo = ReturnInfo(
                                                                 articleInfo = ArticleInfoFlags(duplicateList = False, title = True))))

q.addKeyword('AGL')
data = er.execQuery(q)
print(data)

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
                    "ASX code": "AGL.AX",
                    "Date": datetime.datetime(d_y, d_m, d_d, 0, 0),
                    "URL": str(url),
                    "Title":title,
                    "Body": body
                }
                        
                histo.insert_one(parsart)
                print(parsart)



asx2 = ['ANZ.AX', 'Amcor', 'AMP LTD', 'BHP Billiton', 'Commonwealth Bank', 'CSL.AX', 'Macquarie Group' 'NAB.AX', 'Rio Tinto', 'Scentre', 'Telstra' 'Wespac', 'Wesfarmers', 'Woolworths']
'''''
for name in asx2:

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
                        "Date": datetime.date(d_y, d_m, d_d),
                        "URL": str(url),
                        "Title":str(title),
                        "Body": str(body)
                    }
                        
                    histo.insert_one(parsart)
                    print(parsart)
    news = []
'''''