# import scrapy
#
# import requests, urllib
#
# url = 'https://search.jd.com/Search?keyword=macbookpro&enc=utf-8&page=1'
# headers = {
#     'User=agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
#     'cookie':'shshshfpa=67939ea9-c72d-3766-a9d6-13f88c819152-1533564277; shshshfpb=2789860fd0a654bbd8ff86e20e3f50b765b748f77677d4627956855771; qrsc=3; __jdu=7027267; unpl=V2_ZzNtbURURBFyCRFSfh4MUGIFEl5KUBZBdF9HVCgaDgwyBUEOclRCFX0UR1NnGF8UZAEZWEdcQBVFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZH0YXwNkBBRtclBzJUUITlx%2fHlU1ZjMTbQADHxF9DUJWflRaBGQFEVpEZ0Ildg%3d%3d; areaId=1; __jda=122270672.7027267.1533564261.1546571793.1559490263.38; __jdc=122270672; __jdv=122270672|direct|-|none|-|1559490263059; PCSYCityID=1; xtest=1851.cf6b6759; ipLoc-djd=1-72-2799-0; shshshfp=819014ff2985d8a429fef741180c17cf; rkv=V0900; __jdb=122270672.3.7027267|38.1559490263; shshshsID=a276b6c545caa900023619c3153d6daa_3_1559490457205; 3AB9D23F7A4B3C9B=QUBQRYRYCPBWCEWRJJF6HCQ4YWGQDNOJJ4LNOX6KTZTFZQZPLEUFNVRJ2MXJY4AYQKMWEFQB73WRUEDYOONTNOLEQEupgrade-insecure-requests:1'
# }
# res = requests.get(url, headers=headers)
# res.encoding = 'utf-8'
# html = res.text
#
#
# print(html)
#


import urllib.request
import pymysql
from lxml import etree
from selenium import webdriver
import time
import csv


# 第一步创建一个浏览器对象


def craw():
    browser = webdriver.Chrome()
    url = 'https://www.jd.com/'
    browser.get(url)
    browser.find_element_by_xpath('//*[@id="key"]').send_keys('爬虫')
    browser.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
    time.sleep(3)
    while True:
        objs = browser.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
        print(objs)
        time.sleep(1)
        for obj in objs:
            info = obj.text.split('\n')
            if info[0][0:2] == "每满":
                continue
            elif info[0] == "单件":
                continue
            with open('京东.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([info[0], info[1]])
            print(obj.text)
            print("***********")
        print(type(browser.page_source.find('pn-next disabled')))
        if browser.page_source.find('pn-next disabled') == -1:
            browser.execute_script(
                'window.scrollTo(0,document.body.scrollHeight)'
            )
            time.sleep(1)
            browser.find_element_by_xpath('//*[@id="J_bottomPage"]/span[1]/a[9]').click()
            time.sleep(2)
        else:
            print('结束')
            break



def main():

    craw()



if __name__ == "__main__":
    main()

# browser.execute_script(
#     'window.scrollTo(0,document.body.scrollHeight)'
# )
