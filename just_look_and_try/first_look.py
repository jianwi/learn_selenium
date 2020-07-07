from selenium import webdriver
import time

driver  = webdriver.Chrome()
driver.get("http://jialidun.vip")
time.sleep(2)
driver.get("http://qq.com")
time.sleep(2)
# 返回
driver.back()
time.sleep(1)
# 前进
driver.forward()
time.sleep(3)
# 刷新
driver.refresh()
# 退出
driver.quit()