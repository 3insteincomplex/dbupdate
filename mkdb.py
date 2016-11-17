from pymongo import MongoClient
import datetime
import ystockquote as ysq

asx = ['ABP', 'ACX', 'ABC', 'AGL', 'ALQ', 'ALU', 'AWC', 'AMC', 'AMP', 'ANN', 'APA', 'APN', 'APO', 'ARB', 'AAD', 'ALL', 'AHY', 'ASX', 'AZJ', 'AST', 'ANZ', 'AAC', 'API', 'AHG', 'AOG', 'BOQ', 'BAP', 'BPT', 'BGA', 'BAL', 'BEN', 'BHP', 'BKL', 'BSL', 'BLD', 'BXB', 'BRG', 'BKW', 'BTT', 'BWP', 'CTX', 'CAR', 'CGF', 'CHC', 'CQR', 'CIM', 'CWY', 'CCL', 'COH', 'CBA', 'CPU', 'CTD', 'CGC', 'CCP', 'CMW', 'CWN', 'CSL', 'CSR', 'CYB', 'DXS', 'DMP', 'DOW', 'DUE', 'DLX', 'ECX', 'EHE', 'EVN', 'FXJ', 'FPH', 'FBU', 'FXL', 'FLT', 'FMG', 'GUD', 'GEM', 'GXY', 'GTY', 'GMA', 'GMG', 'GPT', 'GNC', 'GXL', 'GOZ', 'GWA', 'HVN', 'HSO', 'HGG', 'ILU', 'IPL', 'IGO', 'IFN', 'IAG', 'IOF', 'IVC', 'IFL', 'IPH', 'IRE', 'INM', 'ISD', 'JBH', 'A2M', 'JHC', 'JHX', 'LLC', 'LNK', 'MFG', 'MGR', 'MIN', 'MMS', 'MND', 'MPL', 'MQA', 'MQG', 'MTR', 'MTS', 'MYO', 'MYR', 'MYX', 'NAB', 'NCM', 'NEC', 'NSR', 'NST', 'NUF', 'NVT', 'NWS', 'NXT', 'OFX', 'ORA', 'ORE', 'ORG', 'ORI', 'OSH', 'OZL', 'PGH', 'PMV', 'PPT', 'PRY', 'PTM', 'QAN', 'QBE', 'QUB', 'REA', 'REG', 'RFG', 'RHC', 'RIO', 'RMD', 'RRL', 'RSG', 'RWC', 'S32', 'SAI', 'SAR', 'SBM', 'SCG', 'SCP', 'SDF', 'SEK', 'SFR', 'SGM', 'SGP', 'SGR', 'SHL', 'SIP', 'SKC', 'SKI', 'SKT', 'SPK', 'SPO', 'SRX', 'STO', 'SUL', 'SUN', 'SVW', 'SWM', 'SXL', 'SYD', 'SYR', 'TAH', 'TCL', 'TGR', 'TLS', 'TME', 'TNE', 'TPM', 'TTS', 'TWE', 'VCX', 'VOC', 'VRT', 'WBC', 'WEB', 'WES', 'WFD', 'WHC', 'WOR', 'WOW', 'WPL', 'WSA']
1
now = datetime.datetime.now()
past = now - datetime.timedelta(days = 5)
date_delete = past - datetime.timedelta(days=1)
start = past.strftime("%Y-%m-%d")
end = now.strftime("%Y-%m-%d")


delete_d = date_delete.strftime("%Y%m-%d")
del_d  =str(delete_d+"T00:00:00.000Z")
client = MongoClient('mongodb://admin1:admin1@ds059306.mlab.com:59306/heroku_ph242ktw')
db = client.get_default_database()
histo = db['hist_rec']
null = 0

for item in asx:
    code = str(item +".AX")
    hist = ysq.get_historical_prices(code, start, end)

    for i in hist:
        if i != None:
            date = datetime.datetime.strptime(i, "%Y-%m-%d")
            price = hist.get(i, {})
            adj_close =  price.get('Adj Close', {})
            close =  price.get('Close', {})
            opening =  price.get('Open', {})
            low =  price.get('Low', {})
            high =  price.get('High', {})
            vol =  price.get('Vol', {})        
        
            prices = {
                "high":  float(high),
                "open":  float(opening),
                "low":   float(low),
                "adj_close":   float(adj_close),
                "close":   float(close)
            }
            filtered_page = {
                "asx_code": code,
                "date": date,
                "price": prices
            }
            histo.insert_one(filtered_page)
        print(filtered_page)