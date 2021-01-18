#selenium定位网页元素的demo

from selenium import webdriver
EdgeDriver_path = 'D:\Python_SDK\edge_driver\msedgedriver.exe'
driver = webdriver.Edge(executable_path = EdgeDriver_path)
driver.get('http://www.sohu.com/')

# print(driver.page_source)
# print(driver.current_url)
#获取classname为"txt"的页面元素
# elements = driver.find_elements_by_class_name("txt")

# for element in elements:
#     print(element.text)
elements = driver.find_elements_by_xpath('//nav[@class = "nav area"]')

for element in elements:
    print(element.text)


driver.close()