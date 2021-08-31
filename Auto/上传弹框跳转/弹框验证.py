from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
# 创建谷歌浏览器对象
chromeDriver = webdriver.Chrome()

# 打开百度网址
chromeDriver.get("F:\PythonCode\python\Auto\上传弹框跳转\dialogs.html")

# 窗口最大化
chromeDriver.maximize_window()
chromeDriver.find_element_by_id("alert").click()
chromeDriver.switch_to.alert.accept()
# query = chromeDriver.find_element_by_id("alert").click()
# query.send_keys(Keys.ENTER)
time.sleep(2)
chromeDriver.find_element_by_id("confirm").click()
chromeDriver.switch_to.alert.accept()

time.sleep(2)
chromeDriver.quit()


