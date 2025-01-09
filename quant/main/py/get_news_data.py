import requests
import time
from bs4 import BeautifulSoup as bs 
from ..models import cnn_news_model,bbc_news_model,yahoo_news_model

def get_bbc_news():
    bbc_news_model.objects.all().delete()
    data = requests.get("https://push.api.bbci.co.uk/batch?t=%2Fdata%2Fbbc-morph-%7Blx-commentary-data-paged%2Fabout%2F19a1d11b-1755-4f97-8747-0c9534336a47%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F0%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2Fabout%2F19a1d11b-1755-4f97-8747-0c9534336a47%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F1%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2Fabout%2F19a1d11b-1755-4f97-8747-0c9534336a47%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F50%2Fversion%2F1.5.6%7D?timeout=5").json()#網址失效
    data = data['payload'][1]['body']['results']
    for i in range(len(data)):
        new_news = bbc_news_model(title = data[i]['title'] , summary = data[i]['summary'] , url = "https://www.bbc.com"+data[i]['url'] , content = "None")
        new_news.save()

def get_cnn_news():
    cnn_news_model.objects.all().delete()
    response = requests.get("https://edition.cnn.com/business").text
    soup = bs(response,'html.parser')
    for link in ["container__link container_lead-plus-headlines-with-images__link container_lead-plus-headlines-with-images__left container_lead-plus-headlines-with-images__light","container__link container_lead-plus-headlines-with-images__link","container__link container_lead-plus-headlines__link","container__link container_grid-4__link"]:
        data = soup.find_all(class_=link)
        for i in range(len(data)):
            if data[i].find('span',{'data-editable': 'headline'}) == None:
                continue
            new_news = cnn_news_model(title = data[i].find('span',{'data-editable': 'headline'}).text , summary ="None" ,url = "https://cnn.com" + data[i]['href'] , content = "None" )
            new_news.save()

def get_yahoo_news():
    yahoo_news_model.objects.all().delete()
    response = requests.get("https://tw.stock.yahoo.com/news").text #網址失效
    soup = bs(response,'html.parser')
    data = soup.find_all(class_='Ov(h) Pend(14%) Pend(44px)--sm1024')
    for i in range(len(data)):
        new_news = yahoo_news_model(title = data[i].find('a').text , summary = (data[i].find('p').text)[:60] , url = data[i].find('a')['href'] , content = "None")
        new_news.save()
"""
while True:
    get_bbc_news()
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    get_cnn_news()
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    get_yahoo_news()
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    time.sleep(300)
"""
#https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JYcG9MVlJYR2dKVVZ5Z0FQAQ?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant
#https://push.api.bbci.co.uk/batch?t=%2Fdata%2Fbbc-morph-%7Blx-commentary-data-paged%2Fabout%2F19a1d11b-1755-4f97-8747-0c9534336a47%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F0%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2Fabout%2F19a1d11b-1755-4f97-8747-0c9534336a47%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F1%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2Fabout%2F19a1d11b-1755-4f97-8747-0c9534336a47%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F50%2Fversion%2F1.5.6%7D?timeout=5
#https://edition.cnn.com/business

"""
https://cnn.com

container__link container_grid-4__link
container__link container_lead-plus-headlines-with-images__link
container__link container_lead-plus-headlines__link

Ov(h) Pend(14%) Pend(44px)--sm1024
"""
