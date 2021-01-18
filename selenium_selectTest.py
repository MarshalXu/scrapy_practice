#selenium网页下拉菜单操作demo
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge




EdgeDriver_path = 'D:\Python_SDK\edge_driver\msedgedriver.exe'
# driver = webdriver.Edge(executable_path = EdgeDriver_path)

# make Edge headless
edge_options = EdgeOptions()
edge_options.use_chromium = True  # if we miss this line, we can't make Edge headless
# A little different from Chrome cause we don't need two lines before 'headless' and 'disable-gpu'
edge_options.add_argument('headless')
edge_options.add_argument('disable-gpu')
driver = Edge(executable_path=EdgeDriver_path, options=edge_options)

driver.get('http://sahitest.com/demo/selectTest.htm')

#找到需要操作的下拉菜单位置
element = driver.find_element_by_id('s1')

select = Select(element)
select.select_by_index(1)
time.sleep(5)
select.select_by_value('47')
time.sleep(5)
select.select_by_visible_text('Fax')
time.sleep(5)

print(select.all_selected_options)
print(select.first_selected_option)




driver.close()