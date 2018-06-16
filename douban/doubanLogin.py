# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.douban.com/")
driver.find_element_by_id("form_email").send_keys("1138631642@qq.com")
driver.find_element_by_name("form_password").send_keys("yjcdoubanpassword666")
driver.find_element_by_id("captcha_field").send_keys("right")
driver.find_element_by_class_name("bn-submit").click()
driver.save_screenshot("douban.png")