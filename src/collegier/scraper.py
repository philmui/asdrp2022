###############################################################################
# scraper.py
# ----------
# This is a scaper for the college newspaper project. 
#
# @author: Theodore Mui
# @date: Sun Dec 18 17:18:44 PST 2022
###############################################################################

import requests
from bs4 import *
import re
import random
import time

from article import Article

DATE_PATTERN = re.compile("https://stanforddaily.com/(\d+)/(\d+)/(\d+)")
BASE_URL = "https://stanforddaily.com/category/opinions/page/"
HEADER = {'User-Agent': 'Mozilla/5.0'}

def getArticleText(url):
    html = requests.get(url, headers=HEADER).text
    soup = BeautifulSoup(html, 'html.parser')
    lines = soup.get_text().splitlines()
    output = ""
    for line in lines:
        words = re.split('[\s\t]', line)

        if len(words) > 3:
            output += line + '\n'
    return output

def getArticles(baseURL, numPages=10, showProgress=False):
    articles = []
    pageNumber = 1
    hasArticles = True
    while hasArticles and pageNumber <= numPages:
        pageContent = requests.get(baseURL+str(pageNumber), headers=HEADER)
        soup = BeautifulSoup(pageContent.text, "html.parser")
        articleList = soup.select("div > h3 > a[href^='http']")

        if showProgress: print(f"{pageNumber} : {len(articleList)}")
        if len(articleList) <= 0: hasArticles = False
        if hasArticles:
            for article in articleList:
                url = article.get('href')
                date_groups = DATE_PATTERN.search(url)
                
                if article.text != None and len(article.text) > 0:
                    articles.append(Article(
                        article.text, 
                        url,
                        getArticleText(url),
                        int(date_groups.group(1)),
                        int(date_groups.group(2)),
                        int(date_groups.group(3))
                    ))
            pageNumber += 1
            time.sleep(random.randint(0, 100) / 100.0)

    return articles

if __name__ == "__main__":
    articles = getArticles(BASE_URL, numPages=1, showProgress=True)

    for article in articles:
        print(article)
        print(article.content)

    print(f"Total articles found: {len(articles)}")
    print(f"First article has date: {articles[0].date}")
    print(f"First article has date: {articles[len(articles) - 1].date}")
