from selenium import webdriver
import time
# 创建谷歌浏览器对象
chromeDriver = webdriver.Chrome()

# 打开百度网址
chromeDriver.get("F:/PythonCode/python/Auto/autotest.html")

# 窗口最大化
chromeDriver.maximize_window()

chromeDriver.find_element_by_id('accountID').send_keys('zywzyx')
chromeDriver.find_element_by_id('passwordID').send_keys('QAQ')
#换城市
chromeDriver.find_element_by_id('areaID').send_keys('北京市')
time.sleep(1)
chromeDriver.find_element_by_id('areaID').send_keys('天津市')
#性别
chromeDriver.find_element_by_id('sexID2').click()
time.sleep(1)
chromeDriver.find_element_by_id('sexID1').click()
#季节
chromeDriver.find_element_by_xpath("//*[@value='spring']").click()
chromeDriver.find_element_by_xpath("//*[@value='summer']").click()
chromeDriver.find_element_by_xpath("//*[@value='Auterm']").click()
chromeDriver.find_element_by_xpath("//*[@value='winter']").click()
#上传文件
chromeDriver.find_element_by_name('file').send_keys('F:\PythonCode\python\Auto\qwq.png')
#弹窗
chromeDriver.find_element_by_id('buttonID').click()
chromeDriver.switch_to.alert.accept()

time.sleep(3)
chromeDriver.quit()