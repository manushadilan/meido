import scrapy
from meido.items import MeidoItem

class meido(scrapy.Spider):
    name='meido_scraper'
    start_urls=['http://www.vn-meido.com/k1/index.php?board=17.0']

    for i in range(20, 1220, 20):
        start_urls.append("http://www.vn-meido.com/k1/index.php?board=17."+str(i)+"")

    def parse(self,response):

        tr=response.xpath("//*[@id='messageindex']/table/tbody/tr")

        for tdata in tr:
            item=MeidoItem()
            item['subject']=tdata.xpath("td[3]/div/span/a/text()").extract()
            if not item['subject']:
                item['subject']=tdata.xpath("td[3]/div/strong/span/a/text()").extract()

            item['startedBy']=tdata.xpath("td[3]/div/p/a/text()").extract()
            item['link']=tdata.xpath("td[3]/div/span/a/@href").extract()
            if not item['link']:
                item['link']=tdata.xpath("td[3]/div/strong/span/a/@href").extract()
            
            item['replies']=tdata.xpath("normalize-space(td[4]/text()[1])").extract()
            item['views']=tdata.xpath("normalize-space(td[4]/text()[2])").extract()
            item['lastPostDate']=tdata.xpath("normalize-space(td[5]/text()[2])").extract()
            item['lastPostBy']=tdata.xpath("td[5]/a[2]/text()").extract()

            yield item



