class computer:
    screen = ""  #屏幕
    price = ""  #价格
    CPU = ""
    ROM = ""
    time = ""
    action = "打字，打游戏，看视频"

    def run(self):
        print("有屏幕大小:", self.screen,"寸","，价格", self.price,"￥","，cpu型号", self.CPU,"，内存大小",self.ROM,
              'G，待机时长', self.time, "小时的电脑用于",self.action)



c = computer()
c.screen = 18
c.price = 5800
c.CPU = 'i7-8750k'
c.ROM = 8
c.time = 20

c.run()