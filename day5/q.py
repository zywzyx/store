'''
有下列列表，请编程实现列表的数据翻转（京东金融的测试开发笔试题）可以选做
list = [1,2,3,4,5,6,7,8,9]
实现效果：list = [9,8,7,6,5,4,3,2,1]
'''
# i=1
# list_1=[]
# list = [1,2,3,4,5,6,7,8,9]
# while i<=len(list):
#     list_1.append(list[-i])
#     i=i+1
# print(list_1)
'''
请编程统计列表中的每个数字出现的次数(百度初级测试开发笔试题)
List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
'''
# List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
# list_1=set(List)
# count={}
# for i in list_1:
#     count.update({i:List.count(i)})
# print(count)
'''
编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}   （阿里一轮笔试题）
'''
# def number(f):
#     global set
#     set=set(f)
#     count={}
#     for i in f:
#         count.update({i:f.count(i)})
#     print(count)
# number([21,21,21,56,56,56,56,56,56,56,56,56,10,10,10])


# 声明一个列表，在列表中保存6个学生的信息(6个题1中的字典)
students = [
    {'name':'张三','age':23,'score':88,'tel':'23423532','gender':'男'},
    {'name':'李四','age':26,'score':80,'tel':'12533453','gender':'女'},
    {'name':'王五','age':15,'score':58,'tel':'56453453','gender':'男'},
    {'name':'赵六','age':16,'score':57,'tel':'86786785','gender':'保密'},
    {'name':'小明','age':18,'score':98,'tel':'23434656','gender':'女'},
    {'name':'小红','age':23,'score':72,'tel':'67867868','gender':'女'},
]
# 1)	统计不及格学生的个数
# count=0
# for i in range(0,len(students)):
#     if students[i]["score"]<60:
#         count=count+1
# print("不及格的人数：",count)

# 2)	统计未成年学生的个数
# count=0
# for i in range(0,len(students)):
#     if students[i]["age"]<18:
#         count=count+1
# print("未成年的人数：",count)

# 3)	打印手机尾号是8的学生的名字
# for i in range(0,len(students)):
#     if int(students[i]["tel"][-1])==8:
#         print(students[i]["name"])



# 4)	打印最高分和对应的学生的名字
# max=students[0]["score"]
# for i in range(0,len(students)):
#     if max<students[i]["score"]:
#         max=students[i]["score"]
#         print(students[i]["name"])



# 5)	将列表按学生成绩从大到小排序
reverse=True
students = sorted(students, key=lambda x:x['score'])
print(students)




# 6)	删除性别保密的所有学生
# for i in range(0,len(students)):
#     if students[i]["gender"] == "保密":
#         a=i
# students.pop(a)
# print(students)
