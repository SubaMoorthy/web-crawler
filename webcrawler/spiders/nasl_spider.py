import scrapy
from webcrawler.items import NASLPlayer

class NaslSpider(scrapy.Spider):
    name = "nasl"
    allowed_domains = ["nasl.com"]
    start_urls = ["http://www.nasl.com/stats/players/table"]

    def parse(self, response):
        attrlist = []
        scraped_data = []
        table = response.xpath("//table[@id='playerStatsTable']")
        for attr in table.xpath("thead/tr/th/text()"):
            attrlist.append(attr.extract())
        for tr in table.xpath("tbody/tr"):
            i = 0
            item = NASLPlayer()
            
            for td in tr.xpath("td/text()"):
                item[attrlist[i]] = td.extract()
                i = i + 1
            scraped_data.append(item)
        return  scraped_data


