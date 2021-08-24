f = open("user.txt","r")

data = f.readlines()


use = []

for i in data:
    da = i.split(",")
    use.append(da)
    print(da)

name = input("用户名：")
pw = input("密码：")
for i in range(0,len(use)):
    if name ==use[i][0] and pw == use[i][1]:
        print("登录成功")