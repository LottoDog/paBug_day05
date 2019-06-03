#chromedriver无界面模式/添加代理
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    添加代理IP
    options.add_argument('--proxy-server=http://')
    browser = webdriver.Chrome(options=options)
    broswer.get(url)
    
    多线程加锁
    
        多个线程中语句会拆分执行，没有锁会发生不确定性造成结果不准确
        控制操作 临界资源 共享资源时的不确定性
        而全局解释器锁是Python中也会有相同的问题
        
       
    队列 form queue import Queue
    q= Queue()创建队列对象
    q.put(url)
    q.get()退出
    q.empty() 队列对象判断是否为空
    如果队列中没有内容时 再get（）会阻塞
    
    from threading import Thread
    t = Thread(target=函数名)
    t.start()
    t.join()
    
    例子：
        t_list = []
        #列表记录防止阻塞,列表退出
        for i in range(5):
            t = Thread(target=函数名)
            t_list.append(t)
            t.start()
        for j in t_list:
            j.join()#会阻塞
    


#第三方抓包工具
    首先设置
    tool  -->options设置HTTPs(点击ACtions);from browser only不然显示比较多
          -->Connnectons  端口好设为与浏览器一致；Allow remote compters to connect允许远程电脑链接（手机）
    
    chrome装个插件ProxySwitchOmega
    ProxySwitchOmega 新建情景模式 设置127.0.0.1端口与fiddler一致
    流程1
        点击   切换代理
    
    Fiddler常用 菜单 
    Inspector 查看数据包详情
    Headers 请求头
    Webforms
        POST请求的表单数据<body>
        GET请求的参数<QueryString>
    RAW 整个请求显示为文本
    