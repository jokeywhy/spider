# coding=utf-8
from selenium.common.exceptions import TimeoutException
import config
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def selenium_choice():
    driver = config.DRIVER
    element_zuzhi = driver.find_element_by_id('rmenu6')
    element_zuzhi.click()
    element_jigou = driver.find_element_by_css_selector('#menu6item div.ui-iconlink > a')
    # href = element_jigou.get_attribute('href')
    element_jigou.click()
    driver.implicitly_wait(30)
    driver.switch_to_frame('mainframe')
    # ls_zuzhi = driver.find_element_by_id('1001')
    print driver.page_source

def selenium_login():
    driver = config.DRIVER
    driver.get(config.LOGIN_URLS)
    element_user = driver.find_element_by_xpath('//input[@name="user"]')
    element_pwd = driver.find_element_by_id('passText')
    element_pwd2 = driver.find_element_by_id('pass')
    element_user.send_keys('wfx')
    element_pwd.click()
    element_pwd2.send_keys('9731629553')
    driver.find_element_by_id('loginbtn').click()
    html = driver.page_source
    try:
        WebDriverWait(driver, config.TIMEOUT).until(
            EC.presence_of_element_located((By.ID, "rmenu6"))
        )
    except TimeoutException:
        print u'登陆失败'

def run():
    selenium_login()
    selenium_choice()

if __name__ == '__main__':
    run()
