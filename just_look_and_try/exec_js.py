from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

# get url
driver.get("http://jialidun.vip")

js = "alert('i am using selenium execute javascript')"
driver.execute_script(js)
sleep(2)
# 休息2s退出
driver.quit()