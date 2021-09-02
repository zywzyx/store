from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains# ActionChain
import time

driver = webdriver.Chrome()
ac = ActionChains(driver)


driver.get('https://www.taobao.com/')
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="q"]').send_keys('华为P40')
driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
#登录
driver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys('zywzyx')
driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys('123456')
driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
time.sleep(1)
a = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')
ac.click_and_hold(a).move_by_offset(200,0).perform()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()



#

driver.find_element_by_xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div[2]').click()
driver.find_element_by_xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[4]/div/div/dl[2]/dd/ul/li[1]/a').click()
driver.find_element_by_xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[4]/div/div/dl[4]/dd/ul/li[1]/a/span').click()
driver.find_element_by_xpath('//*[@id="J_LinkBasket"]').click()

