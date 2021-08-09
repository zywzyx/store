import random
import sys

##  登录

start = 1
while start <= 3:
    print('第',start,'次登录')
    name = input("请输入用户名:")
    pwd = input("请输入密码:")
    if name == 'admin' and pwd =='root':
       print('登录成功')
       break
    else:
       print('登录失败')
    start = start + 1

if start == 4:
    print('账户已锁定')
    sys.exit()

######## 猜数字
many = 500

num = random.randint(0,300)

while True:
    number = int(input("请输入数字:"))

    if number > num and many >0:
        many = many - 5
        print("大了,扣除金币5，当前金币数：",many)
    elif number < num and many >0:
        many = many - 5
        print("小了,扣除金币5，当前金币数：",many)
    elif number == num:

        many = many + 500
        print("恭喜！你猜对了，数字是:",num,'获得金币500，当前总金币数:',many)
        st = input('如果你想要继续请输入y，结束请输入n.继续游玩花费300金币')
        if st == 'n':
            sys.exit()
        elif st == 'y':
            many = many -300
            num = random.randint(0, 300)
        else:
            print('请填写y/n')
    else:
        print('金币不足')

