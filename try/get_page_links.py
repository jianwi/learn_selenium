from selenium import webdriver

url = "http://www.keju17.com/"

driver = webdriver.Chrome()
driver.get(url)

if driver.current_url != url:
    print("url 发生了变化，可能发生了重定向，当前url为" + driver.current_url)

for a in driver.find_elements_by_tag_name("a"):
    if a.get_attribute("href"):
        print("发现a标签，链接为：" + a.get_attribute("href"))
    else:
        print("发现a标签，没有定位到链接")

for iframe in driver.find_elements_by_tag_name("iframe"):
    if a.get_attribute("src"):
        print("发现ifram标签，链接为：" + a.get_attribute("src"))
    else:
        print("发现iframe标签，没有定位到链接")
