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
import time
import pickle

class data:
    start_urls = []
    for m in range(9, 13):
        start_urls.append("https://www.swimrankings.net/index.php?page=meetSelect&nationId=0&meetType=1&\selectPage=2016_m" \
                          + str(m))
    for m in range(1, 9):
        start_urls.append("https://www.swimrankings.net/index.php?page=meetSelect&nationId=0&meetType=1&selectPage=2015_m" \
                          + str(m))
    def __init__(self):
        """
        self.races = {}
        competitions = self.competition_finder()
        for comp in competitions:
            time.sleep(.2)
            self.competition_extract(comp)
        pickle.dump(self.races, open('save.p', 'rb'))
        """

    def competition_extract(self, url=""):
        session = HTMLSession()
        r = session.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        names = []
        times = []
        count = 1
        """for name in soup.find_all(class_='name'):
            if count % 2 == 0:
                names.append(name.get_text())
            count += 1
        for time in soup.find_all(class_='swimtime'):
            times.append(time.get_text())"""
        swimmer = soup.find(class_='meetResult0')
        while swimmer:
            info = swimmer.contents
            names.append(info[1].string)
            times.append(info[5].string)
            swimmer = swimmer.next_sibling

        title = soup.find(class_='titleLeft').get_text()
        title = title.replace(" ", "_")
        print(title)
        race = {}
        if len(times) < 8:
            return race
        for i in range(len(times)):
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
                    competitions.append("https://www.swimrankings.net/index.php" + url + "&gender=1&styleId=2")
        return competitions

    def test(self):
        x = {'hi': 1, 'wut':2}
        pickle.dump(x, open("save.p", "wb"))

    def test2(self):
        x = pickle.load(open("save.p", "rb"))
        print(x)

x = data()
x.test()
x.test2()