# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsCrawlerQcwyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #招聘名称 1
    job_position_names = scrapy.Field()
    #职位信息 2
    job_position_info = scrapy.Field() 
    #薪资 3
    job_salary = scrapy.Field()
    #职位福利 4
    job_position_welfare = scrapy.Field()
    #经验要求 5
    job_EXP_require = scrapy.Field()
    #学历要求 6
    job_EDU_require = scrapy.Field()
    #公司名称 7
    company_names = scrapy.Field()
    #公司行业 8
    company_industry = scrapy.Field()
    #公司性质 9
    company_type = scrapy.Field()
    #公司人数 10
    company_size = scrapy.Field()
    #公司概况 11
    company_info = scrapy.Field()
    #搜索关键词 12
    search_by = scrapy.Field()
    #search_url 13
    search_url = scrapy.Field()
    #company_locations 14
    company_locations = scrapy.Field()