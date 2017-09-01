import re
import json
from datetime import datetime
import scrapy
from aliexpress_crawler.items import ItemList
from aliexpress_crawler.items import ItemFeedback
from aliexpress_crawler.items import ItemStore


class AliexpressSpider(scrapy.Spider):
    name = "Aliexpress"
    start_urls = ['http://www.aliexpress.com/category/' 
                  + '200000104/strand-bracelets.html?' 
                  + 'isrefine=y&site=glo&g=y&SortType=total_tranpro_desc&' 
                  + 'tag=&shipCountry=US&needQuery=n']
    feedback_api = 'http://feedback.aliexpress.com/display' \
                   + '/evaluationProductDetailAjaxService.htm' \
                   + '?type=default'
    def parse(self, response):
        item = ItemList()
        item_list = response.xpath('//ul[@class="util-clearfix son-list"]/li')
        next_page_url = \
            response \
                .xpath('//a[@class="page-next ui-pagination-next"]/@href') \
                .extract_first()
        if not item_list:
            return
        current_page = \
            response.xpath('//span[@class="ui-pagination-active"]/text()') \
                    .extract()
        for i in item_list:
            item['item_code'] = \
                i.xpath('@qrdata').extract_first().split("|")[1]
            item['item_name'] = \
                i.xpath('*//a[@class="product "]/@title').extract_first()
            item['url'] =  'http:' \
                + i.xpath('*//a[@class="product "]/@href').extract_first()
            item['item_cate'] = re.search('.*category/([0-9]+).*', 
                                          response.url).group(1)
            item['current_page'] = str(current_page[0])
            item['crawl_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            item['rate_star'] = \
                i.xpath('*//span[@class="star star-s"]/@title') \
                .extract_first()
            item['order_num'] = \
                i.xpath('*//em[@title="Total Orders"]/text()') \
                 .extract_first()
            item['price'] = \
                i.xpath('*//span[@itemprop="price"]/text()').extract_first()
            item['ori_price'] = \
                i.xpath('*//del[@class="original-price"]/text()') \
                 .extract_first()
            item['store_url'] = \
                i.xpath(
                    '*//div[@class="store-name util-clearfix"]/a[1]/@href') \
                 .extract_first()
            store_feed_url = \
                i.xpath('*//a[@class="score-dot"]/@href').extract_first()
            if not store_feed_url:
                item['store_feed_url'] = None
            else:
                item['store_feed_url'] = 'http:' + store_feed_url

            index = item['url'].find('.html')
            item['url'] = item['url'][0:index + 5]
            yield scrapy.Request(self.feedback_api 
                                 + '&page=1&productId='
                                 + item['item_code'], 
                                 self.parse_item_feedback)
            yield scrapy.Request('http:' + item['store_url'], 
                                 self.parse_store_info)
            yield item
        if next_page_url:
            yield scrapy.Request('http:' + next_page_url, self.parse)

    def parse_item_feedback(self, response):
        itemFeedback = ItemFeedback()
        data = json.loads(response.text.replace('\\', ''))
        itemFeedback['item_code'] = re.search('.*productId=([0-9]+).*', 
                                              response.url).group(1)
        itemFeedback['current_page'] = data['page']['current']
        itemFeedback['total_page'] = data['page']['total']
        itemFeedback['records'] = data['records']
        yield itemFeedback
        current_page_num = int(itemFeedback['current_page'])
        total_page_num = int(itemFeedback['total_page'])
        # this api only allow to retrieve 200 pages
        if current_page_num < 200 \
           and current_page_num < total_page_num:
            yield scrapy.Request(self.feedback_api
                                 + '&page='
                                 + str(current_page_num + 1)
                                 + '&productId='
                                 + itemFeedback['item_code'],
                                 self.parse_item_feedback)

    def parse_store_info(self, response):
        itemStore = ItemStore()
        itemStore['store_url'] = response.url
        store_info_header = \
            response.xpath('//div[@class="store-header-inner util-clearfix"]')
        itemStore['store_name'] = \
            store_info_header \
                .xpath('*//span[@class="shop-name"]/a[1]/text()') \
                .extract()[0]
        itemStore['store_time'] = \
            store_info_header \
                .xpath('*//span[@class="shop-time"]/em/text()') \
                .extract()[0]
        itemStore['store_num'] = \
            store_info_header \
                .xpath('*//span[@class="store-number"]/text()') \
                .extract()[0]
        itemStore['crawl_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        yield itemStore
