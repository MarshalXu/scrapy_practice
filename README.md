## 本程序仅供学习与交流scrapy和selenium框架交流使用！！！
### 编写时间大约在2021年1月 
## 结构介绍
└───jobs_crawler_QCWY  
    └───spiders  
        └───__init__.py  
        └───qiancheng_spider.py  
    └───__init__.py  
    └───items.py  
    └───middlewares.py  
    └───pipelines.py  
    └───settings.py  
### 主要文件简介
#### qiancheng_spider.py  
    爬虫主逻辑文件，主要是对网页元素进行解析和翻页逻辑的实现。  
#### items.py  
    Define here the models for your scraped items
#### middlewares.py
    Define here the models for your spider middleware  
    主要是重写了JobsCrawlerQcwyDownloaderMiddleware类，配置selenium相关的东西
#### run_qc.py
    在根目录下运行该文件，开始运行。
#### scrapy.cfg
    scrapy框架的配置文件，应放置在根目录下，缺失后scrapy框架无法正常运行。
#### QCWY_.ipynb
    数据分析的notebook，对招聘网站数据进行简单分析

### 本程序未提供爬取的数据。需自行根据需求修改程序爬取。

