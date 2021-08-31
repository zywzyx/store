from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains# ActionChain
import time
driver = webdriver.Chrome()
ac = ActionChains(driver)



driver.get("https://www.jd.com/")
driver.maximize_window()  # 面试题：为啥做最大化？
driver.find_element_by_xpath('//*[@id="key"]').send_keys('华为P40')
driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[2]').click()

#窗口切换
data = driver.window_handles
driver.switch_to.window(data[1])

#添加购物车
driver.find_element_by_xpath('//*[@id="InitCartUrl"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="loginname"]').send_keys('1763*****')
driver.find_element_by_xpath('//*[@id="nloginpwd"]').send_keys('a56816***')
time.sleep(10)
driver.find_element_by_xpath('//*[@id="loginsubmit"]').click()
time.sleep(2)
# a = driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[1]/div[1]')
# ac.click_and_hold(a).move_by_offset(140,0).perform()