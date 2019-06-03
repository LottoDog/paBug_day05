#selenium + phantomjs/Chrome/Firefor
    selenium 
        web自动化测试工具, 可运行在浏览器,根据指令操作
        必须与第三方浏览器配合
        pip3 install selenium 
    phantomjs
        无头/无界面浏览器
        在内存中加载 高效
    安装 允许浏览器需要driver
    phantomjs/chromedriver/geckoddriver
    
    windows:
        phantomjs/chromedriver/geckodriver
        拷贝到Python安装目录的Scripts目录下（目的：添加到系统的环境变量中）
    
    linux
        where python
        sudo cp xxx /user/bin
    
    browser = webdriver.Firefox()
    browser.get(url)
    browser.page_source      查看响应内容
    rowser.page_source .find('xx')
    没有找到返回-1
    
    html搜索字符串
    内容.find('xx')
    
    browser.find_element_by_xpath
    单元素查找
    browser.find_element_by_id('')
    _bu_name('') _by_class_name('')
    _by_xpath('')
    
    多元素
    browser.find_elements_by_xpath/id/_calss_name
    
    节点对象操作
    ele.send_key('') 搜索框发送内容
    ele.click()
    ele.text 文本
    ele.get_attribute('src') 获取节点属性值
    
#抓取京东数据
    调到商品页面后,匹配所有的商品节点对象列表
    节点对象的内容拿出来想办法处理
    下一页）（browser.page_source..）
    ******time.sleep**