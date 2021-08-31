from selenium import webdriver
import time
# 创建谷歌浏览器对象
chromeDriver = webdriver.Chrome()
chromeDriver.get("F:\PythonCode\python\Auto\上传弹框跳转\pop.html")
# 窗口最大化
chromeDriver.maximize_window()
chromeDriver.find_element_by_id('goo').click()

#弹窗切换
data = chromeDriver.window_handles
chromeDriver.switch_to.window(data[1])