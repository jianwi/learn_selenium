from selenium import webdriver


driver = webdriver.Chrome()

driver.get("http://jialidun.vip")

#获取 标题 和当前链接

print(driver.title,driver.current_url)

#通过 dom 获取页面的信息
# print(driver.find_element_by_id("index_text").text)

# 获取所有的 a 标签
print(driver.find_elements_by_tag_name("a"))



