import random

coupon = [
    ["机械革命","机械革命 5折优惠券",0.5]*10,
    ["卫龙辣条","卫龙辣条 3折优惠券",0.3]*20,
    ["HUA WEI WATCH","HUA WEI WATCH 8折优惠券",0.8]*15
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
mm = money #花费金额 = 初始金额 -余额


# 2. 准备一个空的购物车
mycart = []
number =[]
# 3. 准备一个我的优惠券包
mycoupon = []
#抽优惠券
luck = random.randint(0,2)
mycp = coupon[luck]
print("你抽到了:",mycp[1])
mycoupon.append(mycp)
i = 0  #定义优惠券数量
i = i+1 #抽到则加一

# 3.开始购物


while True:
    for key,value in enumerate(shop):
        print(key,value)
    # 请输入您要卖的商品
    chose = input("请输入您要买的商品:")
    if chose =='q':
        break
    num = input("请输入购买数量:")
    number.append("数量："+num)
    num_list = []
    num_list.append(int(num))
    if chose.isdigit():
        chose = int(chose) # "1" --> 1
        if chose > len(shop) or chose < 0: # 9 > 7
            print("该商品不存在！别瞎弄！")
        else:
            for s in range(0, len(mycoupon)):


                if shop[chose][0] in mycoupon[s][0] and money > money - shop[chose][1]*mycoupon[s][2]*int(num) and i >0 and int(num) ==1:  #优惠券内包含所选商品且余额买得起商品，优惠券数量大于0

                    i = i-1
                    money = money - shop[chose][1]*mycoupon[s][2]
                    mycart.append([[shop[chose][0],shop[chose][1]* mycoupon[s][2]]+number])
                    number.pop()
                    print("恭喜，商品添加成功！您的余额为：￥",money)
                    print("输入Q打印小票,结束购物")
                elif shop[chose][0] in mycoupon[s][0] and money > money - shop[chose][1]*mycoupon[s][2]*int(num) and i >0 and int(num)>1:
                    i = i - 1
                    money = money - shop[chose][1] * mycoupon[s][2]
                    nn = float(num)
                    money = money - (shop[chose][1] * nn)
                    mycart.append([shop[chose][0],'%.2f'% (shop[chose][1]*mycoupon[s][2])])
                    n = num_list[0] - 1
                    number.pop()
                    number.append("数量："+str(n))

                    mycart.append([[shop[chose][0], shop[chose][1]] + number])
                    number.pop()
                    print("恭喜，商品添加成功！您的余额为：￥", money)
                    print("输入Q打印小票,结束购物")


                elif money  >= shop[chose][1] and i <= 1: #余额大于所选商品价格，优惠券数量小于1
                      money = money - shop[chose][1]*int(num)
                      mycart.append([shop[chose]+number])

                      number.pop()
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




# 4. 打印结算购物小条

print("以下是您的购物小条，请拿好！！！！么么哒！")
print("".center(30,"-"))
for key,value in enumerate(mycart):
    print(key,value)

HH = mm - money

print("".center(30,"-"))
print("合计花费:",'%.2f' % HH)
print("余额:",money)