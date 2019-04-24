"""
THIS FILE SHOULDN'T BE USED. Should pull the .json files
instead of running this.
Data_Scraper class is made for scraping swimrankings.net
for 100m Freestyle races between 9/2015 and 8/2016.
Writes meet data into .json files.
"""
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import time
import json

class Data_Scraper:

    """
    Initializer runs everything required to scrape and save the data.
    Can only use limited amount of start_urls since the crawler will
    get ipbanned. Quote out as necessary.
    SELF.RACES is a dictionary with a race name as key and another dictionary as value.
    The subdictionary contains swimmers as key and an array with place and time as value.
    """
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
        for m in range(6, 8):
            self.start_urls.append(
                "https://www.swimrankings.net/index.php?page=meetSelect&nationId=0&meetType=1&selectPage=2016_m" \
                + str(m))
        """
        self.start_urls.append("https://www.swimrankings.net/index.php?page=meetSelect&nationId=0&meetType=1&selectPage=2016_m8")
        """

        self.races = {}
        print(self.start_urls)
        competitions = self.competition_finder()
        count = 0
        
        
        for comp in competitions:
            if count % 50 == 1:
                time.sleep(10)
            self.competition_extract(comp)
            count += 1
        with open('result4.json', 'w') as fp:
            json.dump(self.races, fp)


    """ 
    URL defines as specific race webpage to retrieve swimmers and related
    placement information. Places race into SELF.RACES dictionary, with the 
    swimmer and info array subdictionary. 
    Only includes the final result of open races with greater than 7 racers. 
    """
    def competition_extract(self, url=""):
        session = HTMLSession()
        r = session.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        time.sleep(.4)

        names = []
        times = []

        heats = soup.find_all(class_="meetResultHead")
        swimmer = None
        for heat in heats:
            event = heat.contents[0].contents[1]
            if event == "Men, 100m Freestyle, Timed Final,  Open" \
                    or event == 'Men, 100m Freestyle, Final,  Open'\
                    or event == 'Men, 100m Freestyle, Final,  18 years and older':
                swimmer = heat.next_sibling
                break
        if not swimmer:
            return
        while swimmer:
            info = swimmer.contents
            names.append(info[1].string)
            times.append(info[5].string)
            swimmer = swimmer.next_sibling

        title = soup.find(class_='titleLeft').get_text()
        title = title.replace(" ", "_")
        race = {}
        if len(times) < 8:
            return
        for i in range(7):
            if times[i] > times[i + 1]:
                return
        for i in range(len(times)):
            race[names[i]] = [i + 1, times[i]]
        while title in self.races:
            title = title + '1'
        print(title)
        self.races[title] = race

    """
    From the meets page on swimrankings.net, finds long course races
    with full results. 
    """
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
