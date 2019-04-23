import scrapy
class Crawler(scrapy.spider):
    name = "url_finder"
    start_urls = [
        "https://www.swimrankings.net/index.php?page=meetSelect&nationId=0&selectPage=RECENT",
    ]

    def parse_main(self, response):

