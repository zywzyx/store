# 只做页面的操作
class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    # 1.登陆的操作
    def login(self,username,pwd):
        # 输入用户名
        self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        # 输入密码
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys(pwd)
        # 点击登陆
        self.driver.find_element_by_xpath("//*[@id='submit']").click()

    # 获取成功的数据信息
    def get_success_data(self):
        return self.driver.title

    # 获取密码错误信息
    def get_error_pwd_data(self):
        return self.driver.find_element_by_xpath("//*[@id='msg_uname']").text

























