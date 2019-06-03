from threading import Thread
from queue import Queue
import requests
import time
import json


class xiaomi_spider(object):
    def __init__(self):
        # 创建空队列
        # 交友应用页
        self.url = 'http://app.mi.com/categotyAllListApi?page={}&categoryId=2&pageSize=30'
        self.headers = {
            'User-agent': "Mozilla/5.0"
        }
        self.url_queue = Queue()

    def url_in_queue(self):
        for page in range(10):
            url = self.url.format(str(page))
            print(url)
            self.url_queue.put(url)

    # 线程事件函数：请求 解析 保存
    def get_data(self):
        while True:
            # 来一个线程能处理多少队列事件就去多少
            # 从队列中获取url 保证不为空
            if not self.url_queue.empty():
                url = self.url_queue.get()
                # 发送请求 获取响应 提取数据
                html = requests.get(url, headers=self.headers).text
                self.parse_page(html)
            else:
                break

    def parse_page(self, html):
        # JSON loads()将JSOn字符串转为Python格式
        # print(html)
        app_json = json.loads(html)
        print(app_json)
        for app in app_json['data']:
            name = app['displayName']
            link = 'http://app.mi.com/details?id=' + app['packageName']
            d = {'名称': name, '链接': link}
            print(d)
            #存入文件用dump（），逆向字典-->json字符串用dumps（）
            with open('小米.json', 'a') as f:
                #d可以是字典字符串列表，默认是ASCI编码
                json.dump(d, f, ensure_ascii=False)

    def main(self):
        # 所有url入队列
        self.url_in_queue()
        # 创建线程
        t_list = []
        for i in range(1):
            t = Thread(target=self.get_data)
            t_list.append(t)
            t.start()
        # 回收
        for j in t_list:
            j.join()


if __name__ == "__main__":
    start = time.time()
    s = xiaomi_spider()
    s.main()
    end = time.time()
    print("执行时间：%.2f" % (end - start))
