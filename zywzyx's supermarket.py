import random

coupon = [
    ["机械革命","机械革命 5折优惠券",0.5],
    ["卫龙辣条","卫龙辣条 3折优惠券",0.3],
    ["HUA WEI WATCH","HUA WEI WATCH 8折优惠券",0.8]
]

shop = [
    ["lenovo PC",5600],
    ["HUA WEI WATCH",1200],
    ["Mac pro",12000],
    ["洗衣机",3000],
    ["机械革命",5000],
    ["卫龙辣条",4.5],
    ["老干妈辣酱",20],
]

# 1.准备好钱包

money = input("亲输入您的初始余额：")
money = int(money)

# 2. 准备一个空的购物车
mycart = []
# 3. 准备一个我的优惠券包
mycoupon = []
#抽优惠券
luck = random.randint(0,2)
mycp = coupon[luck]
print("你抽到了:",mycp[1])
mycoupon.append(mycp)
# 3.开始购物

i  = 0
while i < 20:
    for key,value in enumerate(shop):
        print(key,value)
    # 请输入您要卖的商品
    chose = input("请输入您要买的商品:")

    if chose.isdigit():
        chose = int(chose) # "1" --> 1
        if chose > len(shop) or chose < 0: # 9 > 7

            print("该商品不存在！别瞎弄！")
        else:
            if shop[chose][0] in mycp[0] and money > money - shop[chose][1]*mycp[2]:

                money = money - shop[chose][1]*mycp[2]
                print("恭喜，商品添加成功！您的余额为：￥",money)
                print("输入Q打印小票,结束购物")

            elif money  > shop[chose][1]:
                money = money - shop[chose][1]
                print("恭喜，商品添加成功！！！！您的余额为：￥",money)
                print("输入Q打印小票,结束购物")

            else:
                print("温馨提示：您的银行卡余额不足，穷鬼！请买其他商品！")
                print("输入Q打印小票,结束购物")


    elif chose == "q" or chose == "Q":
        print("欢迎下次光临！")
        break
    else:
        print("对不起，别瞎弄！重新输入！")

    i = i + 1

# 4. 打印结算购物小条

print("以下是您的购物小条，请拿好！！！！么么哒！")
print("".center(30,"-"))
for key,value in enumerate(mycart):
    print(key,value)
print("".center(30,"-"))