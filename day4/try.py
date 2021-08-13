list_max = []
list_min = []
list1 = []
#输入数组
for i in range(50):
    list = input('请输入数组:').split()
    if len(list)>4:

        print("超出限制")
    else:
        list_int = [int(x) for x in list]
        len(list_int)
        list1.append(list_int)
        k = 0
#行最大值
        for j in list_int:
            if j == max(list_int):
                break
            k = k+1
        list_max.append([i+1, k + 1, max(list_int)])

    if len(list1) == 4:
        print(list1)
        print(list_max)
        break
#列最小值
list2 = [[list1[j][i] for j in range(4)] for i in range(4)]
i = 0
for l in list2:
    i = i +1
    k = 0
    for j in l:
        if j == min(l):
            break
        k = k+1
    list_min.append([k +1 ,i,min(l)])
#求鞍点
for i in list_max:
    for j in  list_min:
        if str(i) == str(j):
            print("鞍点:",i,end="")