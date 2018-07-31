""" 
@file: 02-冒泡.py
@Time: 2018/07/29
@Author:heningqiu
"""
import random

''' 生成乱序列表 random.shuffle '''
lst=[]
for i in range(1,101):
    lst.append(i)
random.shuffle(lst)

a=lst.copy()
# print(a)
# print(sorted(a,reverse=False))
''' 冒泡排序 '''
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1]= a[j+1],a[j]
print(a)
''' 冒泡排序 '''
# for i in range(len(a)):
#     for j in range(i):
#         if a[j] > a[j+1]:
#             a[j],a[j+1]= a[j+1],a[j]
# print(a)

print("*"*30)
print(len(a)) # 100