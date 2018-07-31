""" 
@file: 03-冒泡截取.py
@Time: 2018/07/29
@Author:heningqiu
"""

def func(n):
    pass

num=input("随意请输入20个整数,输出最小的3位数字:")
lst1=list(eval(num))
for i in range(len(lst1)-1):
    for j in range(len(lst1)-1-i):
        if lst1[j] > lst1[j+1]:
            lst1[j],lst1[j+1]=lst1[j+1],lst1[j]
print(lst1)
print(lst1[:3])

