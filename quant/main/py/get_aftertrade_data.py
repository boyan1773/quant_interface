import yfinance as yf
import requests
import time
import random
import pandas as pd

# TWSE
def get_trade_value(stocknumber,date):
    return requests.get(f"https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY?date={date}&stockNo={stocknumber}&response=json").json()

def get_market_data(date):
    return requests.get(f"https://www.twse.com.tw/rwd/zh/afterTrading/FMTQIK?date={date}&response=json").json()

def get_pe_data(stocknumber):
    return requests.get(f"https://www.twse.com.tw/rwd/zh/afterTrading/BWIBBU?date={time.strftime('%Y%m%d',time.localtime())}&stockNo={stocknumber}&response=json").json()

def lastmonthdate(last):
    lastmonth = time.localtime().tm_mon-last
    lastmonth = '%02d' % lastmonth
    year=time.localtime().tm_year
    if time.localtime().tm_mon == 1:
        year-=1
    return f"{year}{lastmonth}01"

def day_data(stocknumber,peroid=6):
    data =[]
    for i in range(peroid-1,-1,-1):
        lastmonth = i
        lastmonth_date = lastmonthdate(lastmonth)
        try:
            trade = get_trade_value(stocknumber,lastmonth_date)
            data = data + trade['data']
            columns=trade['fields']
            time.sleep(random.uniform(0.1,0.5))
            title = trade['title'].split()[2]
        except:
            continue
    try:
        data = pd.DataFrame(data,columns=columns)
    except:
        return None,stocknumber
    data = data.apply(lambda x: x.replace(',', ''))
    return  title,data

def market_data(period=6):
    data = []
    for i in range(period-1,-1,-1):
        lastmonth = i
        lastmonth_date = lastmonthdate(lastmonth)
        try:
            market = get_market_data(lastmonth_date)
            data = data + market['data']
            columns=market['fields']
            time.sleep(random.uniform(0.1,0.7))
        except:
            continue
    df = pd.DataFrame(data,columns=columns)
    df.rename(columns={"發行量加權股價指數":"收盤價"}, inplace=True)
    df = df.apply(lambda x: x.replace(',', ''))
    return df

def pe_data(stocknumber):
    data = get_pe_data(stocknumber)
    df = pd.DataFrame(data['data'][-1],index=data['fields']).transpose()
    df.set_index('日期',inplace=True)
    return df

# Yahoo
def info(stock):
    try:
        stock_ticker=yf.Ticker(f"{stock}.tw")
        info = stock_ticker.info
    except:
        stock_ticker=yf.Ticker(f"{stock}.two")
    info = stock_ticker.info
    dividends = stock_ticker.dividends
    msg=''
    try:
        msg+=f"\n{'-'*9}基本面{'-'*9}\n股利 : {info['dividendRate']}\n追蹤PE : {round(info['trailingPE'],2)}\n預測PE : {round(info['forwardPE'],2)}\n追蹤EPS(近4季) : {info['trailingEps']}\n預測EPS(近4季) : {info['forwardEps']}\nPEG比率 : {info['pegRatio']}"
        msg+=f"\n{'-'*9}分析師{'-'*9}\n目標最高價 : {info['targetHighPrice']}\n目標最低價 : {info['targetLowPrice']}\n目標平均價格 : {info['targetMeanPrice']} \n目標中位數 : {info['targetMedianPrice']}\n推薦評級平均值 : {info['recommendationMean']}"
    except:
        None 
    return(msg)

#https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY?date=20230814&stockNo=2330&response=json
#https://www.twse.com.tw/rwd/zh/afterTrading/BWIBBU?date=20230814&stockNo=2330&response=json
#https://www.twse.com.tw/rwd/zh/afterTrading/FMTQIK?date=20230701&response=json
#https://openapi.taifex.com.tw/v1/DailyForeignExchangeRates