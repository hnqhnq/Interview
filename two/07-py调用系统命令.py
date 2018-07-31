""" 
@file: 07-py调用系统命令.py
@Time: 2018/07/29
@Author:heningqiu
"""
import os
msg=os.popen("ping www.baidu.com").readlines()
print(msg)

m2=os.system('ping www.baidu.com') #此种方法出来编码是乱码
print(m2)


