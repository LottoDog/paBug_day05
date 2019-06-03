import requests
import json

# json中也有一个模块专门处理JSON
# 一级界面：https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1559294508470&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn

# （index变化），时间戳没有检查

level01_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1559294508470&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'


class TecentSpider(object):
    def __init__(self):
        self.headers = {
            'User-agent': 'Mozilla/5.0',

        }
        self.level01_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1559294508470&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'

    def get_page(self, url):
        res = requests.get(url, headers=self.headers)
        res.encoding = 'utf-8'

        # JSON模块使用
        # json.loads()把json--->python数据类型
        html = json.loads(res.text)
        return html

    def parse_01(self, html):
        '''
        html-->dic{data{Posts}}
        '''
        for job in html['Data']['Posts']:
            name = job['RecruitPostName']
            type = job['LocationName']
            id = job['PostId']
            #职责要求在二级页面
            level02_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1559295961384&postId={}&language=zh-cn'.format(id)
            #向二级发送
            duty, job = self.parse_02(level02_url)
            print("===================")
            print(name+'\n'+type+'\n'+duty+'\n'+job+'\n')
            print("===================")

    def parse_02(self,level02_url):
        html = self.get_page(level02_url)

        duty = html['Data']['Responsibility']
        require = html['Data']['Requirement']
        return duty, require

    def main(self):
        for index in range(1, 11):
            url = self.level01_url.format(index)
            html_1 = self.get_page(url)
            self.parse_01(html_1)

if __name__ == "__main__":
    s = TecentSpider()
    s.main()


