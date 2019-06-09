import requests
from bs4 import BeautifulSoup
import pandas as pd

url ='https://www.yitutech.com/en/news'
response= requests.get(url)
#response.encoding = 'UTF-8'
wbdata = response.text
soup = BeautifulSoup(wbdata,'lxml')


#获取翻页
#div.page >
page_list=[]
for i in range(0,7):
    url_page='https://www.yitutech.com/en/news?page='+str(i)
    #print(url_page)
    page_list.append(url_page)
print(page_list)

list=[]
#获取1-6页的新闻网址
for urlpage in page_list:
    response = requests.get(urlpage)
    response.encoding = 'UTF-8'
    page_url_content = response.text
    soup_url = BeautifulSoup(page_url_content, 'lxml')

    for news in soup_url.select('a.flex'):
        href = news['href']
        # print(href)
        url = 'https://www.yitutech.com' + href
        #print(url)
        list.append(url)
print(list)
print(len(list))




#获取每条新闻的标题、时间和内容
#标题：div.news-title.flex
#时间：div.middle > span.date-display-single
#内容：div.nr


time=[]
title=[]
news_content=[]
for url in list:
  response = requests.get(url)
  response.encoding = 'UTF-8'
  each_news_content = response.text
  soup_content = BeautifulSoup(each_news_content, 'lxml')
  title_include_time = soup_content.select('div.news-title.flex')[0]
  title1=title_include_time.select('h2')[0].text
  title.append(title1)
  #print(title)
  time_step_1 = soup_content.select('div.middle ')[0]
  time1 = time_step_1.select('span.date-display-single')[0].text
  time.append(time1)
  #print(time)
  news_content1 = soup_content.select('div#nr')[0].text
  #print(news_content)
  news_content.append(news_content1)

#爬下来的时间，标题和内容都是一个list，将list合并成dictionary，
# 将dictionary转变成dataframe，再将dataframe打印成csv
dic={'time':time, 'title':title,'news_content':news_content}
#print(dic)
df=pd.DataFrame(dic)
#print(df)
df.to_csv("/home/cqiuac/AI_in/yitu_news_English.csv",
          index=True,sep=',',encoding='utf_8_sig')

