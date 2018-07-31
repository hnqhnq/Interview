""" 
@file: 05_时间装饰器.py
@Time: 2018/07/22
@Author:heningqiu
"""
import time

'''
写一个装饰器，传入一个秒数，如果函数执行完成超过这个数值显示bad，否则显示good
'''

def warp(t):
    def inner(func):
        def inner_t(*args,**kwargs):
            start=time.clock()
            func(*args,**kwargs)
            end=time.clock()
            if end-start>t:
                print('bad')
            else:
                print('good')
        return inner_t
    return inner

@warp(1)
def func(*args,**kwargs):
    for i in range(1000000):
        pass
func()

'''
原函数：打印电话号码
1.需求：给我的原函数添加一个装饰器，装饰器的功能，判断电话号码是否合法
'''
def  isLegal(func):
    def inner(pnum):
        if len(pnum) != 11 or not pnum.isdigit() or not pnum.startswith("1"):
            print("电话号码不合法")
            pnum = None
        return func(pnum)#执行原函数
    return inner

#原函数
@isLegal
def  printNum(pnum):
    print(pnum)
printNum("2345678901")


