from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains# ActionChain
import time
driver = webdriver.Chrome()
ac = ActionChains(driver)



driver.get("https://www.qcc.com/")
driver.maximize_window()  # 面试题：为啥做最大化？
#点击登录，
driver.find_element_by_link_text("登录 | 注册").click()
time.sleep(2)
#鼠标滑动
a = driver.find_element_by_class_name("nc-lang-cnt")
ac.click_and_hold(a).move_by_offset(348,0).perform()
time.sleep(1)
#弹框点击关闭
driver.find_element_by_xpath("//*[@id='loginModal']/div/div/div/button").click()

#
# driver.refresh()
# time.sleep(5)
#鼠标悬停
# b = driver.find_element_by_class_name('dropdown-toggle')
# ac.move_to_element(b).perform()