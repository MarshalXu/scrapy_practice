#selenium实现网页操作的demo

from selenium import webdriver
from selenium.webdriver.common import action_chains
import time

#声明edge_driver路径
EdgeDriver_path = 'D:\Python_SDK\edge_driver\msedgedriver.exe'

#创建webdriver对象
driver = webdriver.Edge(executable_path = EdgeDriver_path)
driver.get('http://sahitest.com/demo/clicks.htm')

#找到网页中按钮的位置
click_btn = driver.find_element_by_xpath('//input[@value = "click me"]') #左键单击
double_click_btn = driver.find_element_by_xpath('//input[@value = "dbl click me"]') #左键双击
right_click_btn = driver.find_element_by_xpath('//input[@value = "right click me"]') #右键单击

actionChains = action_chains.ActionChains(driver)
actionChains.click(click_btn).double_click(double_click_btn).context_click(right_click_btn).perform()
time.sleep(10)

print(driver.find_element_by_xpath('//textarea').get_attribute('value'))


driver.close()