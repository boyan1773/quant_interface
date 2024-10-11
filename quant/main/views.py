from django.shortcuts import render
from .py.get_aftertrade_data import day_data,pe_data,market_data
from .py.index import ema,kd,rsi,cdp,bias,volume_ratio,ma5,ma20
from .py.get_news_data import get_bbc_news,get_cnn_news,get_yahoo_news
from .models import cnn_news_model,bbc_news_model,yahoo_news_model

def index(request):
    data = market_data()

    data = ema(data)
    data = ma5(data)
    data = ma20(data)

    bias_n = bias(data)
    rsi_n = rsi(data)
    volume_r = volume_ratio(data)

    date = (data.iloc[-1])["日期"]
    index = (data.iloc[-1])["收盤價"]
    change = (data.iloc[-1])["漲跌點數"]

    chart = data[["日期","收盤價","成交股數","ema","ma5","ma20"]]
    context = {
        'chart':chart.to_json(orient="split"),
        'date':date,
        'index':index,
        'change':change,

        'rsi':round(rsi_n.iloc[-1],2),
        'bias':bias_n.iloc[-1],
        'volume_ratio':volume_r,
    }
    return render(request,"index.html",context)

def search(request):
    stocknumber = request.GET.get('n')

    title,data = day_data(stocknumber)
    if title == None:
        return render(request,"detail/error.html",locals())
    data = ema(data)
    data = ma5(data)
    data = ma20(data)

    k_line , d_line = kd(data)
    rsi_n = rsi(data)
    volume_r = volume_ratio(data)
    c,r1,r2,s1,s2 = cdp(data)
    bias_n = bias(data)

    day = data[["日期"]]
    change = (data.iloc[-1])["漲跌價差"]
    close = float((data.iloc[-1])["收盤價"].replace(',', ''))
    open = float((data.iloc[-1])["開盤價"].replace(',', ''))
    high = float((data.iloc[-1])["最高價"].replace(',', ''))
    lowset = float((data.iloc[-1])["最低價"].replace(',', ''))
    print(close)

    cols_to_convert = ["收盤價", "成交股數", "開盤價", "最高價", "最低價", "ema", "ma5", "ma20"]
    data[cols_to_convert] = data[cols_to_convert].replace(',', '', regex=True).astype(float)
    chart = data[["日期"] + cols_to_convert][19:]    
    
    context = {
        'stocknumber':stocknumber,
        'title':title,
        'day':day,
        'change':change,
        'close':close,
        'open':open,
        'high':high,
        'lowset':lowset,
        'chart':chart.to_json(orient="split"),

        'k_line':k_line[-1],
        'd_line':d_line[-1],
        'rsi':round(rsi_n.iloc[-1],2),
        'volume_ratio':volume_r,
        'bias':bias_n.iloc[-1],

        'cdp':round(c.iloc[-1],2),
        'r1':round(r1.iloc[-1],2),
        'r2':round(r2.iloc[-1],2),
        's1':round(s1.iloc[-1],2),
        's2':round(s2.iloc[-1],2),
        }
    try:
        pe= pe_data(stocknumber)
        context['yiel'] = (pe.iloc[-1])["殖利率(%)"]
        context['peratio'] = (pe.iloc[-1])["本益比"]
        context['pbr'] = (pe.iloc[-1])["股價淨值比"]
    except:
        return render(request,"detail/detail_etf.html",context)
    return render(request,"detail/detail_stock.html",context)

def stock(request):
    return render(request,"stock.html",locals())    

def etf(request):
    return render(request,"etf.html",locals())

def news(request):
    return render(request,"news/news.html",locals())

def cnn_news(requset):
    get_cnn_news()
    data = cnn_news_model.objects.values()
    d = {}
    for i in range(len(data)):
        d[i]=data[i]
    context={'data':d}
    return render(requset,"news/cnn_news.html",context)

def bbc_news(request):
    get_bbc_news()
    data = bbc_news_model.objects.values()
    d = {}
    for i in range(len(data)):
        d[i]=data[i]
    context={'data':d}
    return render(request,"news/bbc_news.html",context)

def yahoo_news(request):
    get_yahoo_news()
    data = yahoo_news_model.objects.values()
    d = {}
    for i in range(len(data)):
        d[i]=data[i]
    context={'data':d}
    return render(request,"news/yahoo_news.html",context)

#0056 00712