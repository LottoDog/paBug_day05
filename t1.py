from selenium import webdriver
import time
#第一步创建一个浏览器对象
browser = webdriver.Chrome()

#打开网页
browser.get('http://www.baidu.com')

#点击搜索按钮，休眠5s 关闭
# browser.find_element_by_id('kw')
browser.find_element_by_xpath('//*[@id="kw"]').send_keys('美女')
time.sleep(1)
browser.find_element_by_xpath('//*[@id="su"]').click()
time.sleep(5)
browser.quit()
# browser.save_screenshot('百度.png')