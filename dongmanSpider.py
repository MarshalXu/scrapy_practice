# -*- coding: utf-8 -*-
'''
# Created on 04-11-22 15:26
# @Filename: dongmanSpider.py
# @Desp: 
# @author: xuc
'''
import requests
from bs4 import BeautifulSoup
import os
root_dir = os.path.dirname(os.path.abspath(__file__))
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.57"
    }


def crawler(url):
    r =requests.get(url=url,headers=head)
    r.encoding = "gbk"
    data = r.text

    s = BeautifulSoup(data,"html.parser")
    li_list = s.find_all("div", class_ = "slist")

    if li_list != []:
        count = 0
        endfix = li_list[0].find_all("img")
        for li in endfix:
            img = "https://pic.netbian.com/" + li["src"]
            # img = "https://pic.netbian.com/" + li.find("img").get("src")
            title = li["alt"]
            rr = requests.get(img)
            with open(root_dir + "/res/page%s_%s_no%s.jpg" %(("1" if url[-6] == "n" else url[-6]),title,count) ,"wb") as f:
            # with open(f"{count}.jpg","wb") as f:
                f.write(rr.content)
            count+=1
if __name__ == "__main__":

    urls = ["https://pic.netbian.com/4kdongman/"] + ["https://pic.netbian.com/4kdongman/index_{}.html".format(i) for i in range(2,168) ]
    # urls = ["https://pic.netbian.com/4kdongman/index_{}.html".format(i) for i in range(0,5) ]
    for url in urls:
        crawler(url)