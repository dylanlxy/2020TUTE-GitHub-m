
'''
def numble(x):
    sum_1 = 0
    for i in range(x):
        if i % 3 == 0 or i % 5 == 0:
            sum_1 += i
    return sum_1
print(numble(int(input("请输入一个数"))))

'''
'''
a=0
for n in range(1,10):
    if n%3==0 or n%5==0:
        a=a+n
print(a)

'''

'''
# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 生成第一个随机数
#print("random() : ", random.randint(1,100))

# 生成第二个随机数
# print("random() : ", random.random())


import random
def a():
    b = random.randint(1,100)
    print("随机数是：",b)
    c = int(input("请输入一个整数："))
    count = 1
    while  c!= b:
        if c > b:
            print("数字太大")
        elif c < b:
            print("数字太小")
        count += 1
        c = int(input("请输入一个整数："))
    print("恭喜您，您猜对了！您一共猜了%d次" % count)
a()
'''

'''
#2020-9-2 周三 下午 13：58 python  0319

a = 0
b = 1
i = 0
tmp = 0
num = 7

while i < num:
 #   olda = a
 #   a = b
 #   b = olda + b
    a,b = b,a+b
    print(a)
    i += 1
'''
''' 
#continue and break

for i in range(10):
    print(i)
    if i == 6:
        break
    if i == 3:
        continue
    print(1000)
'''

'''
for i in range(10):
    print(i)
    if i == 6:
        break
    if i == 3:
        continue
    if i == 5:
        pass
    print(1000)
'''

'''
list = []
list_1 = input('请输入值，结束请按q：')
while(list_1 != 'q'):
    list.append(list_1)
    print(list)
    list_1 = input('请输入值，结束请按q：')
'''
'''
list = []
list_1 = input('请输入值，结束请按q：')
while(list_1 != 'q'):
    list.append(list_1)
    list_1 = input('请输入值，结束请按q：')
print(list)
'''
'''
l = []
while 1:
    b = input('Please input your information:')
    if b == 'q':
        break
    else:
        l.append(b)
print(l)
'''
'''
lists = [1,3,4,5,6,7,9,2]
# 切片
print(lists[::-1])
# 函数reverse 对数组进行操作
lists.reverse()
print(lists)
# 函数reversed 返回一个迭代对象，需要list化
print(list(reversed(lists)))
'''

#篮球记分系统
huren = []
zhongguo = []
print('****************NBA比赛记分系统****************')
dui = input('请选择得分球队：湖人队【1】 中国队【2】')
def fenshu():

    if dui == '1':
        while 1:
            defen = input("您选择的是【湖人队】请输入得分：")
            if denfen == 'q':
                fenshu()
            else:
                defen = int(fenshu)
                huren.append(denfen)
    elif dui == '2':
        while 1:
            defen = input("您选择的是【中国队】请输入得分：")
            if denfen == 'q':
                fenshu()
            else:
                defen =int(fenshu)
                zhongguo.append(defen)





fenshu()

print(fenshu)








