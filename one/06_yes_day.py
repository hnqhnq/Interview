""" 
@file: 06_yes_day.py
@Time: 2018/07/22
@Author:heningqiu
"""
'''
7.编写代码获取昨天的日期，格式：2018-01-03
'''
import datetime
now_time=datetime.datetime.now()
yes_time=now_time+datetime.timedelta(days=-1)
yes_time_nyr=yes_time.strftime('%Y-%m-%d')
print(yes_time_nyr)

'''
查看一下程序的运行结果：
总结：
双层装饰器：先运行被装饰的函数头部，中间加插入装饰器函数，最后运行被装饰函数结果
'''
def decorator_a(func):
    print('Get in decorator_a##')
    def inner_a(*args,**kwargs):
        print("Get in inner_a###")
        return func(*args,**kwargs)
    return inner_a

def decorator_b(func):
    print('Get in decorator_b**')
    def inner_b(*args, **kwargs):
        print('Get in inner_b***')
        return func(*args, **kwargs)
    return inner_b
@decorator_a
@decorator_b
def f(x):
    print('Get in f')
    return x*2
f(1)
'''
Get in decorator_b**
Get in decorator_a##
Get in inner_a###
Get in inner_b***
Get in f
'''

