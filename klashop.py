# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLText(newsurl):
    try:
        r = requests.get(newsurl,timeout=30)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getProduct(goodsList,html):
    result = {}
    res = requests.get(newsUrl)
    res.encoding = 'UTF-8'
    soup = BeautifulSoup(res.text,'html.parser')
    result['sku'] = soup.select('a')[0]['href']       #获取商品的sku
    result['title'] = soup.select('a')[0]['title']    #商品的标题
    result['price'] = soup.select('.cur ')[0].text     #商品的价格
    return result
#   没用函数设计，提取商品信息的部分，一步一步的提取信息
# res = requests.get('http://www.kaola.com/search.html?key=%25E5%25A5%25B6%25E7%25B2%2589&pageNo=1&type=0&pageSize=60&isStock=false&isSelfProduct=false&isDesc=true&brandId=&proIds=&isSearch=0&isPromote=false&backCategory=&country=&headCategoryId=&needBrandDirect=true&lowerPrice=-1&upperPrice=-1&changeContent=pageNo#topTab')
# res.encoding='utf-8'
# soup = BeautifulSoup(res.text,'html.parser')
# for news in soup.select('.goods'):
#     a = news.select('a')[0]['href']
#     title = news.select('a')[0]['title']
#     price = news.select('.cur ')[0].text
#     print a,title.encode('utf-8'),price.encode('utf-8')

def printPage(goodsList):      #设计打印格式
    tplt='{:6}\t{:8}\t{:16\t{:8}'      #设计字段的占位数，
    print(tplt.format("序号","商品sku","商品名称","商品价格"))
    for i in range(len(goodsList)):
        goods = goodsList[i]
        print(tplt.format(i+1,goods[0],goods[1],goods[2]))

def main():        #主函数
    depth = 2             #遍历的页面数
    goodsList = []              #将商品信息存入goodList中
    for i in range(depth):       #遍历分页函数的设计
        url = 'http://www.kaola.com/search.html?key=%25E5%25A5%25B6%25E7%25B2%2589&pageNo={}&type=0&pageSize=60'   #查看网页翻页的规则其中{}挖空部分为规律部分
        newsurl = url.format(i)
        html = getHTMLText(newsurl)     #url传入
        getProduct(goodsList, html)
    printPage(goodsList)     #商品信息通过设定格式打印出来

main()
