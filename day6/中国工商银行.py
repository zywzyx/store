import string,random,sys
# from nicetry import takemoneyww
from brank import IABC

#信息显示模板
info = '''
 ------------个人信息----------------
 账号：%s,
 用户名：%s,
 密码：******,
 地址信息：
     国家：%s,
     省份：%s,
     城市：%s,
     街道：%s,
     门牌号：%s,
 余额：%s,
 开户行：%s
 -----------------------------------
     '''

#主页
def interface():
    print('*********************')
    print('*    中国工商银行\t\t*')
    print('*    账户管理系统\t\t*')
    print('*      v1.0\t\t\t*')
    print('*********************')
    print('*1.开户\t\t\t\t*')
    print('*2.存钱\t\t\t\t*')
    print('*3.取钱\t\t\t\t*')
    print('*4.转账\t\t\t\t*')
    print('*5.查询\t\t\t\t*')
    print('*6.bye!\t\t\t\t*')
    print('*********************\n')





Code = []
brankUser = {'中国工商银行':[{"账户":"2222","姓名":"zyw","密码":"2222","存款":500},{"账户":"3333","姓名":"zyx","密码":"3333","存款":500},{"账户":"4444","姓名":"zy","密码":"4444","存款":500}]}
userlist = {'2222':[{'国家':'中国','省份':'河北','城市':'唐山','街道':'中山路','门牌号':'010'}],'3333':[{'国家':'中国','省份':'河南','城市':'唐山','街道':'中山路','门牌号':'011'}],'4444':[{'国家':'中国','省份':'河北','城市':'唐山','街道':'中山路','门牌号':'011'}]}
money = 0


#开户

def user():
    # 随机生成账号
     userCode = ''.join(random.sample(string.digits, 8))
     print('账号:',userCode)
     userName = input('请输入姓名:')
     userPwd = input('请输入密码:')
     brankname = '中国工商银行'
     Country = input('请输入国家:')
     Province = input('请输入省份:')
     City = input('请输入城市:')
     Street = input('请输入街道:')
     Table = input('请输入门牌号:')
     if userCode not in Code:
          Code.append(userCode)
          if userName not in brankUser:
              brankUser[brankname].append({"账户":userCode,"姓名":userName,"密码":userPwd,"存款":0})
              userlist[userCode]=[{'国家': Country, '省份':Province,'城市':City,'街道':Street,'门牌号':Table}]
              print('开户成功！！！\n',brankUser)
              print(info % (userCode, userName, Country, Province, City, Street, Table, money, brankname))


          return 1

     elif  len(brankUser[brankname]) == 100:
          print("该银行用户已满")
          return 3
     else:
         if userName in brankUser:
             print('用户已存在！\n', brankUser)
         return 2




#存款
def putMoney():
   code = input('请输入账户:')
   for i in range(0,len(brankUser['中国工商银行'])):
       if code == brankUser['中国工商银行'] [i] ['账户']:
          money = float(input('请输入金额:'))
          brankUser['中国工商银行'] [i] ["存款"] += money
          print('存款成功，总金额为:',brankUser['中国工商银行'] [i] ["存款"])

          return True
   else:
      print('不存在')




#取钱
def getMoney():
    code = input('请输入账户:')
    pwd  = input('请输入密码:')
    for i in range(0,len(brankUser['中国工商银行'])):
        if code == brankUser['中国工商银行'] [i] ['账户'] and pwd == brankUser['中国工商银行'] [i] ['密码']:
            money = float(input('请输入取款金额'))
            if money < brankUser['中国工商银行'] [i] ['存款']:
                brankUser['中国工商银行'][i]['存款'] -= money
                print('取款成功，总余额为:', brankUser['中国工商银行'][i]["存款"])
                return 0
            else:
                print('余额不足！')
                return 3
    else:
        print('账户或密码错误！')
        return 1



#跨行转账
def takemoneyee(account2,tranmoney):

    for i in range(0, len(brankUser['中国工商银行'])):
        if account2 == brankUser['中国工商银行'][i]['账户']:
            for j in range(0, len(brankUser['中国工商银行'])):
                brankUser['中国工商银行'][j]['存款'] += tranmoney
               # print('工行',account2,tranmoney)
                #print(brankUser['中国工商银行'][j])

                return 7
        else:
          #  print('账号不存在')
            return 8







#转钱
def transferMoney():
    code = input('请输入转出账户:')
    pwd = input('请输入密码:')
    for i in range(0, len(brankUser['中国工商银行'])):
        if code == brankUser['中国工商银行'][i]['账户'] and pwd == brankUser['中国工商银行'][i]['密码']:
            transferCode = input('请输入转入账户:')
            for j in range(0, len(brankUser['中国工商银行'])):
                if transferCode == brankUser['中国工商银行'][j]['账户']: #跨省转账
                    if userlist[code][0]['省份'] == userlist[transferCode][0]['省份']:
                        money = float(input('请输入转出金额:'))
                        if money < brankUser['中国工商银行'][j]['存款']:
                            ask = input("确定转账吗？y:确定  n:取消")
                            if ask == 'y':
                                brankUser['中国工商银行'][i]['存款'] -= money
                                brankUser['中国工商银行'][j]['存款'] += money
                                print('转账成功，总余额为:', brankUser['中国工商银行'][i]["存款"])
                                return 0
                            elif ask =='n':
                                print("取消转账")
                            else:
                                print('请输入y/n')
                                return False
                        else:
                             print('余额不足')
                             return False
                    else:
                        money = float(input('请输入转出金额:'))
                        if money+money*0.1 < brankUser['中国工商银行'][j]['存款']:
                            ask = input("确定转账吗？y:确定  n:取消")
                            if ask == 'y':
                                brankUser['中国工商银行'][i]['存款'] -= money * 0.1
                                brankUser['中国工商银行'][j]['存款'] += money
                                print('转账成功，总余额为:', brankUser['中国工商银行'][i]["存款"])
                                return 0
                            elif ask =='n':
                                print("取消转账")
                            else:
                                print('请输入y/n')
                                return False
                        else:
                            print('余额不足')
                            print('转出金额:',money+money*0.1,'包含手续费0.1')
                            return 3
            if transferCode != brankUser['中国工商银行'][j]['账户']:   #跨行转账
                from 农行 import takemoneyww
                moneyy = float(input('请输入转出金额:'))
                #print('农行0', moneyy, transferCode)
                print(moneyy)
                cd = int(transferCode)
                #print(cd)

                s = takemoneyww(cd,moneyy)
                if s == 1:
                    brankUser['中国工商银行'][i]['存款'] -= moneyy
                    print("转账成功，余额为:",brankUser['中国工商银行'][i]['存款'])
                    return False
                elif s == 0:
                    print("账号不存在")
                    return False


            # else:
            #     print("转入账户不存在!!")
            # return True
    else:
        print('账户或密码错误！')
        return 1



#查询

def selectUser():
    code = input('请输入账户:')
    pwd = input('请输入密码:')
    for i in range(0, len(brankUser['中国工商银行'])):
        if code == brankUser['中国工商银行'][i]['账户'] and pwd == brankUser['中国工商银行'][i]['密码']:
            #print( brankUser['中国工商银行'][i])
            for j in range(0, len(userlist[code])):
                #print(userlist[code][j])
                print(info % (brankUser['中国工商银行'][i]['账户'], brankUser['中国工商银行'][i]['姓名'],
                              userlist[code][0]['国家'], userlist[code][0]['省份'], userlist[code][0]['城市'],
                              userlist[code][0]['街道'], userlist[code][0]['门牌号'], brankUser['中国工商银行'][i]['存款'], '中国工商银行'))

            return
    else:
        print('账户或密码错误！')


#退出
def exit():
    print('感谢您的使用，下次再见！')
    sys.exit()









#选项
def index():
  from 农行 import information
  while True:
     interface()
     choose = int(input('输入序号以选择使用的功能:'))

     if choose == 1:
       user()
     elif choose ==2:
         putMoney()
     elif choose ==3:
         getMoney()
     elif choose ==4:
         transferMoney()
     elif choose ==5:
         selectUser()
     elif choose ==6:
         information()


#index()

if __name__ == '__main__':
    index()
