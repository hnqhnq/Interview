""" 
@file: 04-10乘10数组.py
@Time: 2018/07/29
@Author:heningqiu
"""
import numpy as np
a=np.array(np.random.randint(0,1,100).reshape(10,10))
print(a)
a[0,0]=1
print("a1=a[0,0]\n",a)
