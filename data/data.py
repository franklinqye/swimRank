from bs4 import BeautifulSoup
import re
import json
import math
import itertools
from operator import itemgetter
from collections import defaultdict
import datetime

class data:
    def __init__(self):
        

    def page_extract(self, html):
        with open("test.html") as fp:
            soup = BeautifulSoup(fp, 'html.parser')

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
