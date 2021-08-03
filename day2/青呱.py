sum = 0 #一共爬了多少
i = 3 #白天爬的距离
k = 2 #晚上掉 距离
day = 0 #爬的天数
while sum <= 20:
    if sum + i < 20:
       sum = sum - k
       day = day + 1
    sum = sum + i
print('青蛙爬',day,'天可以爬出去')





###################################################################


s=0
l=0

while (20-s)>0:
    s=s+3
    if s>=20:
        break
    s=s-2
    if s>=20:
        break
    l=l+1
print("青蛙第",l,"天能出来")