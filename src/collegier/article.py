###############################################################################
# article.py
# ----------
# This is a class to store an article for the scraper project. 
# 
# @author: Theodore Mui
# @date: Sun Dec 18 17:18:44 PST 2022
###############################################################################

import datetime

class Article: 

    def __init__(self, title, url, content, year, month, day):
        self.title = title
        self.url = url
        self.content = content
        self.year = year
        self.month = month
        self.day = day

    @property
    def date(self):
        return datetime.datetime(self.year, self.month, self.day)

    def __str__(self):
        return f"{self.title}: {self.year}-{self.month}-{self.day}"
