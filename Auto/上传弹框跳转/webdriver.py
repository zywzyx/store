from selenium import webdriver
import time
# 创建谷歌浏览器对象
chromeDriver = webdriver.Chrome()

# 打开百度网址
chromeDriver.get("https://www.bilibili.com/")

# 窗口最大化
chromeDriver.maximize_window()

#跳转框架页
#chromeDriver.switch_to.frame("")

#寻找搜索输入框
#chromeDriver.find_element_by_id("nav_searchform").send_keys("java")
chromeDriver.find_element_by_class_name("nav-search-keyword").send_keys("java")
# 点击百度一下按钮
#chromeDriver.find_element_by_id("from_source").click()
chromeDriver.find_element_by_class_name("nav-search-btn").click()
#窗口切换
data = chromeDriver.window_handles
chromeDriver.switch_to.window(data[1])
#清空文本框
chromeDriver.find_element_by_id("search-keyword").send_keys("")
chromeDriver.find_element_by_id("search-keyword").clear()

chromeDriver.find_element_by_id("search-keyword").send_keys("python")
#chromeDriver.find_element_by_class_name("search-button").click()

a=chromeDriver.find_element_by_class_name("search-button")
chromeDriver.execute_script("arguments[0].click();",a)
# time.sleep(3)
# 退出浏览器
# chromeDriver.quit()