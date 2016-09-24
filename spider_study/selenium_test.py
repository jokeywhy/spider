# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 简单请求
def selenium_normal():
    browser = webdriver.Chrome()
    browser.get('http://www.baidu.com/')

# 页面交互
def selenium_moni():
    driver = webdriver.Chrome()
    driver.get('http://www.python.org')
    assert "Python" in driver.title
    elem = driver.find_element_by_name('q')
    elem.send_keys('pycon')
    elem.send_keys(Keys.RETURN)
    elem.clear() # 清楚输入文本
    print driver.page_source

# 填充表单
def selenium_form():
    driver = webdriver.Chrome()
    driver.get('http://oa.hsu.edu.cn/login.shtml')
    element_user = driver.find_element_by_xpath('//input[@name="user"]')
    element_pwd = driver.find_element_by_id('passText')
    element_pwd2 = driver.find_element_by_id('pass')
    element_user.send_keys('admin')
    element_pwd.click()
    element_pwd2.send_keys('admin')
    driver.find_element_by_id('loginbtn').click()

# 元素拖拽,找不到实例，先放下。。表示的是从source拖动到target的操作
def selenium_drag():
    driver = webdriver.Chrome()
    driver.get('http://xxx.xxx.xxx.xxx')
    element = driver.find_element_by_name('source')
    target = driver.find_element_by_name('target')

    from  selenium.webdriver import ActionChains
    action_chains = ActionChains(driver)
    action_chains.drag_and_drop(element, target).perform()

# 页面切换， 其中windowsname, 可以先通过handler获取之后然后再以数组的方式保存
def selenium_switch():
    driver = webdriver.Chrome()
    driver.switch_to.window('windowName')
    # handler 获取每个窗口对象
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
    # frame 窗口的切换, 焦点切换到一个name为child的frame上
    driver.switch_to.frame('frameName.0.child')
    # 弹窗的处理
    alert = driver.switch_to.alert()

# 历史纪录 控制页面前进或后退
def selenium_history():
    driver = webdriver.Chrome()
    driver.forward()#前进
    driver.back()# 后退

# cookie处理
def selenium_cookies():
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    # 发送cookie
    cookie = {'name':'foo', 'value':'bar'}
    driver.add_cookie(cookie)
    # 获取页面cookie
    driver.get_cookie()

# 页面等待, 两种显式等待（指定某个条件，设置时间，时间内没找到元素，抛出异常），隐式等待（简单的等待时间）
def selenium_wait():
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    # 显示等待
    driver = webdriver.Chrome()
    driver.get('http://somedomain/url_that_delays_loading')
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.ID, "myDynamicElement")) # presence...为显式等待条件
        )
    finally:
        driver.quit()
    # 隐式等待
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # seconds
    driver.get("http://somedomain/url_that_delays_loading")
    myDynamicElement = driver.find_element_by_id("myDynamicElement")

# Phantom的浏览器使用
def selenium_Phantom():
    driver = webdriver.PhantomJS()
    driver.get('http://www.baidu.com')
    print driver.page_source

if __name__=='__main__':
    # selenium_normal()
    # selenium_moni()
    # selenium_form()
    selenium_Phantom()