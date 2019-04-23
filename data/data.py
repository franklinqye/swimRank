from bs4 import BeautifulSoup
import re
import json
import math
import itertools
from operator import itemgetter
from collections import defaultdict
import datetime
import requests
from requests_html import HTMLSession

class data:
    def __init__(self):
        self.races = {}

    def page_extract(self, html=""):
        session = HTMLSession()
        r = session.get(html)
        soup = BeautifulSoup(r.content, 'html.parser')

        names = []
        count = 0
        for name in soup.find_all(class_='name'):
            if count % 2 == 0:
                names.append(name.get_text())
            count += 1
        times = []
        for time in soup.find_all(class_='swimtime'):
            times.append(time.get_text())
        print(names)
        print(times)

        title = soup.find(class_='titleLeft').get_text()
        title = title.replace(" ", "_")
        print(title)
        race = {}
        for i in range(8):
            race[names[i]] = [i + 1, times[i]]
        self.races[title] = race

    def page_finder(self):


x = data()
x.page_extract("https://www.swimrankings.net/index.php?page=meetDetail&meetId=596227&gender=1&styleId=2")
print(x.races)