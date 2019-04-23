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
    start_urls = ["https://www.swimrankings.net/index.php?page=meetSelect&nationId=0&meetType=1&selectPage=2015_m9"]
    def __init__(self):
        self.races = {}

    def page_extract(self, url=""):
        session = HTMLSession()
        r = session.get(url)
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

    def competition_finder(self):
        competitions = []
        for url in data.start_urls:
            session = HTMLSession()
            r = session.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            possi_meets = soup.find_all('td', class_="course", string="50m")
            full_quality = soup.find_all(src="images/meetQuality5.png")[-1]
            count = 0
            for meet in possi_meets:
                quality_indicator = meet.previous_sibling.previous_sibling.contents[0]
                if quality_indicator == full_quality:
                    url = meet.parent.find_all('a')[1].get('href')
                    print(url)
                    competitions.append("https://www.swimrankings.net/index.php" + url)
            return competitions


x = data()
#x.page_extract("https://www.swimrankings.net/index.php?page=meetDetail&meetId=596227&gender=1&styleId=2")
x.page_finder()
#print(x.races)