from bs4 import BeautifulSoup
from requests_html import HTMLSession
import time
import json

class Data_Scraper:

    def __init__(self):
        self.start_urls = []
        """
        for m in range(9, 13):
            self.start_urls.append("https://www.swimrankings.net/index.php?page=meetSelect&nationId=0&meetType=1&selectPage=2015_m" \
                              + str(m))
        for m in range(1, 4):
            self.start_urls.append("https://www.swimrankings.net/index.php?page=meetSelect&nationId=0&meetType=1&selectPage=2016_m" \
                              + str(m))

        for m in range(4, 6):
            self.start_urls.append("https://www.swimrankings.net/index.php?page=meetSelect&nationId=0&meetType=1&selectPage=2016_m" \
                              + str(m))
        """
        for m in range(6, 9):
            self.start_urls.append(
                "https://www.swimrankings.net/index.php?page=meetSelect&nationId=0&meetType=1&selectPage=2016_m" \
                + str(m))

        self.races = {}
        print(self.start_urls)
        competitions = self.competition_finder()
        count = 0
        
        
        for comp in competitions:
            if count % 50 == 1:
                time.sleep(10)
            self.competition_extract(comp)
            count += 1
        #pickle.dump(self.races, open('save.p', 'wb'))
        with open('result4.json', 'w') as fp:
            json.dump(self.races, fp)


    def competition_extract(self, url=""):
        session = HTMLSession()
        r = session.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        time.sleep(.4)

        names = []
        times = []
        count = 1

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
        while title in self.races:
            title = title + '1'
        self.races[title] = race

    def competition_finder(self):
        competitions = []
        for url in self.start_urls:
            time.sleep(.4)
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

if __name__ == '__main__':
    Data_Scraper()
