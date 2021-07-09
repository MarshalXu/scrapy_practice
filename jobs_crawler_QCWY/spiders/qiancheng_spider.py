import scrapy
from selenium import webdriver
from selenium.webdriver.common import action_chains
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
from ..items import JobsCrawlerQcwyItem

import time 
import re

EdgeDriver_path = 'E:\\Python_SDK\\edge_driver\\msedgedriver.exe'


class QianchengSpiderSpider(scrapy.Spider):
    name = 'qiancheng_spider'
    allowed_domains = ['jobs.51job.com','search.51job.com']
    start_urls = [
        # #数据挖掘
        'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E6%258C%2596%25E6%258E%2598,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=',
        #数据分析
        'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=',
        #算法
        'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E7%25AE%2597%25E6%25B3%2595,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=',
        #深度学习
        'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%25B7%25B1%25E5%25BA%25A6%25E5%25AD%25A6%25E4%25B9%25A0,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=',
        #机器学习
        'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%259C%25BA%25E5%2599%25A8%25E5%25AD%25A6%25E4%25B9%25A0,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=',
        # #人工智能
        'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E4%25BA%25BA%25E5%25B7%25A5%25E6%2599%25BA%25E8%2583%25BD,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
    ]
    page_count = [0,0,0,0,0,0]

#
    def __init__(self):
        super(QianchengSpiderSpider,self).__init__()
        # make Edge headless
        edge_options = EdgeOptions()
        edge_options.use_chromium = True  # if we miss this line, we can't make Edge headless
        # A little different from Chrome cause we don't need two lines before 'headless' and 'disable-gpu'
        edge_options.add_argument('headless')
        edge_options.add_argument('disable-gpu')
        self.driver = Edge(executable_path=EdgeDriver_path, options=edge_options)

    def close(self):
        self.driver.quit()
        print('======>close spider')

    def parse(self, response):
        # print("================>hah")
        # print(response.url)
        # print(type(response.body),len(response.body))

        #获取职位名称的list
        position_name_lists = response.xpath('//*[@class = "jname at"]/text()').extract()
        # print(position_name_lists)
        #获取公司地址的list
        loscation_lists = response.xpath('//span[@class = "d at"]/text()').extract()
        # print(loscation_lists)

        # #抓取每个标签页下有多少页数据
        # all_pages = response.xpath('//div[@class = "p_in"]/span/text()').extract_first()
        # page_partten ="[0-9]*"
        # all_pages = int(re.findall(page_partten,all_pages)[2])
        # print('====>',all_pages,type(all_pages))

        #记录搜索标签
        search_by = response.xpath('/html/head/title/text()').extract_first()
        search_by = search_by[1:5]
        if(search_by == "数据挖掘"):
            self.page_count[0] += 1
        elif(search_by == "数据分析"):
            self.page_count[1] += 1
        elif(search_by == "算法招聘"):
            self.page_count[2] += 1
        elif(search_by == "深度学习"):
            self.page_count[3] += 1
        elif(search_by == "机器学习"):
            self.page_count[4] += 1
        elif(search_by == "人工智能"):
            self.page_count[5] += 1
        print('====>',search_by)
        print("1.数据挖掘 第%d页\n2.数据分析 第%d页\n3.算法招聘 第%d页\n4.深度学习 第%d页\n5.机器学习 第%d页\n6.人工智能 第%d页"%\
            (self.page_count[0],self.page_count[1],self.page_count[2],self.page_count[3],self.page_count[4],self.page_count[5]))

        #获取当前页职业的详情页的url_list
        detail_page_lists = response.xpath('//div[@class = "j_joblist"]/div/a/@href').extract()
        # print(detail_page_lists,len(detail_page_lists))
        for idx,detail_page_list in enumerate( detail_page_lists ):
            job_position_name = position_name_lists[idx]#传入职位名称
            company_location = loscation_lists[idx] #传入公司地址
            yield scrapy.Request(detail_page_list,callback=self.parse_detail,meta = {'search_by':search_by,
                                                                                     'job_position_name':job_position_name,
                                                                                     'company_location':company_location})
        #有页码 "e_icons i_next" 最后一页 "e_icons i_next disabled"
        #先判断是否为最后一页
        #再翻下一页
        not_last_page = len(response.xpath('//a[@class = "e_icons i_next"]/@class').extract())
        #如果最后一页 not_last_page == 0 如果不是最后一页 not_last_page > 0
        print(not_last_page)
        if not_last_page:
            self.driver.get(response.url) #selenium
            click_btn = self.driver.find_element_by_xpath('//a[@class = "e_icons i_next"]') #定位单击下一页按钮
            actionChains = action_chains.ActionChains(self.driver)
            actionChains.click(click_btn).perform()
            currentPageUrl = self.driver.current_url
            # print(currentPageUrl)
            yield scrapy.Request(currentPageUrl,callback=self.parse) # scrapy

    def click_next_page(self,response):
        pass

    def parse_detail(self, response):
        #构建items
        item = JobsCrawlerQcwyItem()
        #招聘名称 1
        item['job_position_names'] = response.meta['job_position_name']
        #职位信息 2
        item['job_position_info'] = "".join(response.xpath('//div[@class = "bmsg job_msg inbox"]//text()').extract()).strip()
        #薪资 3
        item['job_salary'] = response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/strong/text()').extract()
        #职位福利 4
        item['job_position_welfare'] = response.xpath('//div[@class = "t1"]/span/text()').extract()
        #经验要求 5
        item['job_EXP_require'] = response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()[2]').extract_first().strip()
        #学历要求 6
        item['job_EDU_require'] = response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()[3]').extract_first().strip()
        #公司名称 7
        item['company_names'] = response.xpath('//div[@class = "com_msg"]/a/p/@title').extract_first()
        #公司行业 8
        item['company_industry'] = response.xpath('//div[@class = "com_tag"]/p[3]/@title').extract()
        #公司性质 9
        item['company_type'] = response.xpath('//div[@class = "com_tag"]/p[1]/text()').extract()
        #公司人数 10
        item['company_size'] = response.xpath('//div[@class = "com_tag"]/p[2]/text()').extract()
        #公司概况 11
        item['company_info'] = "".join(response.xpath('//div[@class = "tmsg inbox"]/text()').extract()).strip()
        #搜索来源 12
        item['search_by'] = response.meta['search_by']
        #url 13
        item['search_url'] = response.url
        #公司地址 14
        item['company_locations'] = response.meta['company_location']
        #向框架传出item
        yield item


