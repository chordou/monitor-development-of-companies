import requests
from bs4 import BeautifulSoup
import pandas as pd
#爬sensetime的英文新闻
url ='https://www.sensetime.com/en/' #爬取中文的，英文的网站https://www.sensetime.com/en/，不过新闻只有四页
response= requests.get(url)
#response.encoding = 'UTF-8'
wbdata = response.text

soup = BeautifulSoup(wbdata,'lxml')
#print(wbdata)

#不用用这个，第一页新闻也有跟2-7页一样的html
# #div.text > a
# list=[]
# #获取第一页的官方新闻链接
# for news in soup.select('div.text '):
#     a = news.select('a')
#     #print(a)
#     href = a[0]['href']
#     #print(href)
#     url='https://www.sensetime.com/'+href
#     #print(url)
#     list.append(url)
# #print(list)

#获取翻页
#div.page >
page_list=[]
for i in range(1,5):
    url_page='https://www.sensetime.com/en/news/index/p/'+str(i)+'.html'
    #print(url_page)
    page_list.append(url_page)
print(page_list)
# for page in soup.select('div.page '):
#     a = page.select('a')
#     #print(a)
#     for i in range(4):
#       href = a[i]['href']
#     #print(href)
#       url_page='https://www.sensetime.com/'+href
#       #print(url_page)
#       page_list.append(url_page)
# #print(page_list)

list=[]
#获取1-4页的新闻网址
for urlpage in page_list:
    response = requests.get(urlpage)
    response.encoding = 'UTF-8'
    page_url_content = response.text
    soup_url = BeautifulSoup(page_url_content, 'lxml')

    for news in soup_url.select('div.text '):
        a = news.select('a')
        # print(a)
        href = a[0]['href']
        # print(href)
        url = 'https://www.sensetime.com/' + href
        #print(url)
        list.append(url)
print(list)
print(len(list))



#获取每条新闻的标题、时间和内容
#标题：h1.new-title

time=[]
title=[]
news_content=[]
for url in list:
  response = requests.get(url)
  response.encoding = 'UTF-8'
  each_news_content = response.text
  soup_content = BeautifulSoup(each_news_content, 'lxml')
  title1 = soup_content.select('h1.new-title ')[0].text
  title.append(title1)
  #print(title)
  time1 = soup_content.select('p.new-time ')[0].text
  time.append(time1)
  #print(time)
  news_content1 = soup_content.select('div.new-nr-con')[0].text
  #print(news_content)
  news_content.append(news_content1)

dic={'time':time, 'title':title,'news_content':news_content}
#print(dic)
df=pd.DataFrame(dic)
print(df)
df.to_csv("/home/cqiuac/AI_in/sensetime_news_English.csv",
          index=True,sep=',',encoding='utf_8_sig')

import json
import html
import urllib
import sys
import re
import random
import time
from threading import Timer

fileOb = open('/home/cqiuac/AI_in/sensetime.txt','w',encoding='utf-8')#打开一个文件若没有就新建一个
for new in news_content:
	fileOb.write(new)
	fileOb.write('\n')
fileOb.close()#关闭文件












