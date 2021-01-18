import scrapy
from ..items import GaobanjiItem
real_small_payload = []
real_big_payload = []
item =  GaobanjiItem()
class GqSpider(scrapy.Spider):
    name = 'GQ'
    # allowed_domains = ['222.236.46.45/nfsdb/COMS/GOCI/L2/2020']
    start_urls = ['http://222.236.46.45/nfsdb/COMS/GOCI/L2/2020/']
    

    def parse(self, response):
        
        #第一层爬取月份的url
        month_urls = response.xpath('/html/body/pre/a/@href').extract()
        #month_url[5] - month_url[8]是5月到8月的url
        #print(month_urls)
        for idx,month_url in enumerate(month_urls):
            month_url = "http://222.236.46.45/" + month_url
            if idx == 5 or idx == 7:
                #拼接url
                #print(month_url)
                yield scrapy.Request(month_url,callback=self.parse_big_flip)
            if idx == 6 or idx == 8:
                #print(month_url)
                yield scrapy.Request(month_url,callback=self.parse_small_flip)
 
    #处理大月翻页的回调
    def parse_big_flip(self,response):
        big_month_urls = response.xpath('/html/body/pre/a/@href').extract()
        for i in range(1,32):
            big_month_day_url = "http://222.236.46.45/" + big_month_urls[i] + 'L2/'
            print(big_month_day_url)
            yield scrapy.Request(big_month_day_url,callback=self.parse_big_month)

    #处理小月翻页的回调
    def parse_small_flip(self,response):
        small_month_urls = response.xpath('/html/body/pre/a/@href').extract()
        for i in range(1,31):
            small_month_day_url = "http://222.236.46.45/" + small_month_urls[i] + 'L2/'
            print(small_month_day_url)
            yield scrapy.Request(small_month_day_url,callback=self.parse_small_month)


    #处理大月网页的回调
    def parse_big_month(self,response):
        # global real_big_payload
        # global item

        all_big_payloads = response.xpath('/html/body/pre/a/@href').extract()
        for idx,all_big_payload in enumerate(all_big_payloads):
            all_big_payloads[idx] = "http://222.236.46.45" + all_big_payload


        real_big_payload.append(all_big_payloads[-1])
        print('====>enter parse_big_month ')
        print(real_big_payload,len(real_big_payload))

        # if(len(real_big_payload) >= 62):
        #     item['month_5_7_last'] = '\n'.join(real_big_payload)
        #     yield item

        

    #处理小月网页的回调
    def parse_small_month(self,response):
        # global real_small_payload
        # global item

        all_small_payloads = response.xpath('/html/body/pre/a/@href').extract()
        for idx,all_small_payload in enumerate(all_small_payloads):
            all_small_payloads[idx] = "http://222.236.46.45" + all_small_payload

        real_small_payload.append(all_small_payloads[-1])
        print('====>enter parse_small_month ')
        print(real_small_payload,len(real_small_payload),len(real_big_payload))

        if(len(real_small_payload) >= 60 and len(real_big_payload) >= 62 ):
            item['month_6_8_last'] = '\n'.join(real_small_payload)
            yield item
        

        
        
        

