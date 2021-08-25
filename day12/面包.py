
import time
from threading import Thread
bread = 500


class cook(Thread):
    cookname = ""
    def run(self) -> None:
        global bread

        s = 0
        while True:
            if bread <500:
                bread = bread +1
                s = s+1
                print("面包篮还有", bread, "个面包",self.cookname,"做了",s,"个面包")
            elif bread == 500:
                time.sleep(2)



class user(Thread):
    username = ""

    def run(self) -> None:
        global bread
        money = 30
        count = 0
        while True:
            if bread >0:
                if money>0:
                    bread = bread - 1
                    money = money - 3
                    count = count +1
                    print(self.username,"抢购成功，已抢购",count,"个面包")
                    #time.sleep(3)
                else:
                    print(self.username,"余额不足，结束抢购")
                    break
            else:
                print("面包不足，请等待师傅补充")
                time.sleep(3)

p1 = cook()
p1.cookname = "康师傅"
p2 = cook()
p2.cookname = "李师傅"
p3 = cook()
p3.cookname = "王师傅"
u1 = user()
u1.username ="小张"
u2 = user()
u2.username = "小刘"
u3 = user()
u3.username = "小赵"
u4 = user()
u4.username = "小王"
u5 = user()
u5.username = "小舞"
u6 = user()
u6.username = "小南"

p1.start()
p2.start()
p3.start()
u1.start()
u2.start()
u3.start()
u4.start()
u5.start()
u6.start()
