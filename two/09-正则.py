""" 
@file: 09-正则.py
@Time: 2018/07/29
@Author:heningqiu
"""
import re

import numpy as np

a=np.array(np.random.randint(0,100,50).reshape(2,5,5))

print(np.array(np.random.randint(0,100,50).reshape(2,5,5)))
print("******")
for i in range(5):
    print(a[:,:,i])
    bb=a[:, :, i]

print("******")

'''用正则匹配在单引号或者双引号中任意文本的方法
（注：单引号里可能存在双引号，双引号里也可能存在单引号）
'''
wen="haha'哈哈\"六\"厉害'dd'我是多余的'd"
a = "[\'\"](.*?)[\'\"]"
print(re.findall(a,wen)) #['哈哈', '厉害', '我是多余的']



