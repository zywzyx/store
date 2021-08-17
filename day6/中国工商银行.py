'''
跨地区转账利率1%
'''

info='''
------------个人信息----------------
账号：%s,
用户名：%s,
密码：******,
地址信息：
    国家：%s,
    省份：%s,
    街道：%s,
    门牌号：%s,
余额：%s,
开户行：%s
-----------------------------------
'''
def page():
    print("*************************************")
    print("*           中国工商银行              *")
    print("*           账户管理系统              *")
    print("*              V1.0                 *")
    print("*************************************")
    print("*1、开户                             *")
    print("*2、存钱                             *")
    print("*3、取钱                             *")
    print("*4、转账                             *")
    print("*5、查询                             *")
    print("*6、Bye!                            *")
    print("*"*37)

account=["2222","3333"]
user ={"中国工商银行":[{"账号":"2222","姓名":"赵四","密码":"2222","存款":500},{"账号":"3333","姓名":"王五","密码":"3333","存款":1000}]}
usersity={"2222":[{"国家":"中国","省份":"北京市","街道":"昌平","门牌号":"301"}],"3333":[{"国家":"中国","省份":"河南","街道":"郑州","门牌号":"302"}]}

#开户
def addname():
    import random
    str = ""
    for i in range(8):
        card=chr(random.randrange(ord("0"), ord("9") - 1))
        str=str +card
    name=input("请输入您的姓名：")
    key=input("请输入账户密码：")
    country = input("请输入国家：")
    province = input("请输入省份：")
    street = input("请输入街道：")
    house = input("请输入门牌号：")
    sity=country+province+street+house
    money=int(input("请输入初始存入金额："))
    brank = "中国工商银行"
    if str not in account:
        if name not in user:
            account.append(str)
            user[brank].append({"账号":str,"姓名":name,"密码":key,"存款":money})
            usersity[str]=[{"国家":country,"省份":province,"街道":street,"门牌号":house}]
            print("开户成功！以下是您的开户信息：")
            print(info % (str,name,country,province,street,house,money,brank))
            return 1

    elif len(account) >100:
        print("银行账户已满！")
        return 3
    else:
        if name in user:
            print("用户已存在！")
            return 2

#存钱
def save_money():
    brankcard=input("请输入您的账户：")
    for i in range(0,len(user["中国工商银行"])):
        if brankcard==user["中国工商银行"][i]["账号"]:
            deposit = float(input("请输入需要存入的金额："))
            user["中国工商银行"][i]["存款"]=user["中国工商银行"][i]["存款"]+deposit
            print("存款成功！")
            print("您的账户余额为：",user["中国工商银行"][i]["存款"])
            return True
    else:
        print("账户不存在！")
        return False

#取钱
def get_money():
    brankcard = input("请输入您的账户：")
    if brankcard in account:
        for i in range(0,len(user["中国工商银行"])):
            if brankcard==user["中国工商银行"][i]["账号"]:
                pwd = input("请输入账户密码：")
                if brankcard==user["中国工商银行"][i]["账号"] and pwd==user["中国工商银行"][i]["密码"]:
                    deposit = float(input("请输入需要取出的金额："))
                    if deposit<=user["中国工商银行"][i]["存款"]:
                        user["中国工商银行"][i]["存款"]=user["中国工商银行"][i]["存款"]-deposit
                        print("取款成功！")
                        print("您的账户余额为：",user["中国工商银行"][i]["存款"])
                    else:
                        print("账户余额不足！")
                        return 3
                elif brankcard==user["中国工商银行"][i]["账号"]:
                    print("账号密码错误！")
                    return 2
    else:
        print("账户不存在！")
        return 1

#跨行转账
def take_money(card,deposit):
    for i in range(0,len(account)):
        if card==user["中国工商银行"][i]["账号"]:
            user["中国工商银行"][i]["存款"]=user["中国工商银行"][i]["存款"]+deposit
            return 1
        else:
            return 2


#转账
def make_money():
    out_card=input("请输入转出的银行账号：")
    up_card=input("请输入转入的银行账号：")
    if out_card and up_card in account:
        pwd=input("请输入转出的银行账号密码：")
        for i in range(0,len(user["中国工商银行"])):
            if out_card==user["中国工商银行"][i]["账号"] and pwd==user["中国工商银行"][i]["密码"]:
                deposit = float(input("请输入转账的金额："))
                deposit_1=deposit*1.01
                if deposit_1 <= user["中国工商银行"][i]["存款"]:
                    if usersity[out_card][0]["省份"]==usersity[up_card][0]["省份"]:
                        user["中国工商银行"][i]["存款"]=user["中国工商银行"][i]["存款"]-deposit
                        for v in range(0, len(user["中国工商银行"])):
                            if up_card == user["中国工商银行"][v]["账号"]:
                                user["中国工商银行"][v]["存款"] = user["中国工商银行"][v]["存款"] + deposit
                        print("转账成功！")
                        print("转出的账户余额为：", user["中国工商银行"][i]["存款"])
                        return True
                    else:
                        user["中国工商银行"][i]["存款"] = user["中国工商银行"][i]["存款"] - deposit_1
                        for v in range(0, len(user["中国工商银行"])):
                            if up_card == user["中国工商银行"][v]["账号"]:
                                user["中国工商银行"][v]["存款"] = user["中国工商银行"][v]["存款"] + deposit
                        print("转账成功！")
                        print("转出的账户余额为：", user["中国工商银行"][i]["存款"])
                        return True
                else:
                    print("转出的银行账户余额不足！")
                    return 3
            elif out_card==user["中国工商银行"][i]["账号"]:
                print("转出的银行账户密码错误！")
                return 2
    elif out_card in account and up_card not in account:    #跨行转账
        pwd = input("请输入转出的银行账号密码：")
        for i in range(0, len(user["中国工商银行"])):
            if out_card == user["中国工商银行"][i]["账号"] and pwd == user["中国工商银行"][i]["密码"]:
                deposit = float(input("请输入转账的金额："))
                deposit_1 = deposit * 1.05
                if deposit_1 <= user["中国工商银行"][i]["存款"]:
                    from 中国农业银行 import take_money
                    s=take_money(up_card, deposit)
                    if s==1:
                        user["中国工商银行"][i]["存款"]=user["中国工商银行"][i]["存款"]-deposit_1
                        print("转账成功！")
                        print("转出的账户余额为：", user["中国工商银行"][i]["存款"])
                        return True
                    elif s==2:
                        print("账号不存在")
                        return False
                else:
                    print("转出的银行账户余额不足！")
                    return 3

            elif out_card==user["中国工商银行"][i]["账号"]:
                print("转出的银行账户密码错误！")
                return 2
    else:
        print("账号不存在！")
        return 1

#查询
def look_user():
    brankcard = input("请输入查询的账号：")
    if brankcard in account:
        pwd = input("请输入账号密码：")
        for i in range(0,len(user["中国工商银行"])):
            if brankcard==user["中国工商银行"][i]["账号"] and pwd==user["中国工商银行"][i]["密码"]:
                print(info % (user["中国工商银行"][i]["账号"],user["中国工商银行"][i]["姓名"],usersity[brankcard][0]["国家"],usersity[brankcard][0]["省份"],usersity[brankcard][0]["街道"],usersity[brankcard][0]["门牌号"],user["中国工商银行"][i]["存款"],"中国工商银行"))
                # print("-------------账户信息---------------")
                # print("账号：",user["中国工商银行"][i]["账号"])
                # print("密码：",user["中国工商银行"][i]["密码"])
                # print("余额：",user["中国工商银行"][i]["存款"])
                # print("用户居住地址：",usersity[brankcard][0]["国家"]+usersity[brankcard][0]["省份"]+usersity[brankcard][0]["街道"]+usersity[brankcard][0]["门牌号"])
                # print("开户行：中国工商银行")
                # print("----------------------------------")
            elif brankcard==user["中国工商银行"][i]["账号"]:
                print("银行账号密码错误！")
    else:
        print("该用户不存在！")


def interface():
    while True:
        page()
        choose = int(input("请选择需要办理的业务:"))
        if choose ==1:
            addname()
        elif choose ==2:
            save_money()
        elif choose ==3:
            get_money()
        elif choose ==4:
            make_money()
        elif choose ==5:
            look_user()
        elif choose==6:
            print("Bye!")
        elif choose ==7:
            from 中国农业银行 import look_userr
            look_userr()
            break
        else:
            print("请正确输入要办理的业务！")
# interface()

if __name__ == '__main__':
    interface()