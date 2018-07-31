""" 
@file: 01_基础函数输出.py
@Time: 2018/07/22
@Author:heningqiu
"""
'''1.在python3环境下运行一下代码，输出？'''
print( round (1.5) )
print( round(2.5) )
print( round(101,-1) )
'''
2
2
100
'''
print("-------------我是分割线--------------")
'''2.写出下面程序 的输出结果：'''
def ChangeInt(a):
    a=10
nfoo = 2
ChangeInt(nfoo)
print(nfoo)
''' 2 '''
def ChangeList(a):
    a[0]=10
IstFoo=[2]
ChangeList(IstFoo)
print(IstFoo)
''' [10] '''
print("-------------我是分割线--------------")
'''3.使用列表推导优化一下代码：'''
result=[]
for x in range(10):
    result.append(x**2)
print(result)
'''答：'''
print([ x**2 for x in range(10) ])
'''
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
'''
print("-------------我是分割线-----test---------")
'''
【规律：
①凡事函数内部进行列表取值再赋值运算则可改变原值，
②函数内部做直接的赋值，不会影响全局变量的原值】
'''
def ChangeList(a):
    for i in range(3):
        a[0]+=10
IstFoo=[1]
ChangeList(IstFoo)
print(IstFoo)
''' [31] '''
def ChangeList(a):
    a=100
IstFoo=[1]
ChangeList(IstFoo)
print(IstFoo)
''' [1] '''
def ChangeList(a):
    for i in range(3):
        a+=10
IstFoo=1
ChangeList(IstFoo)
print(IstFoo)
'''1 '''
print("-------------我是分割线--------------")

'''
7.写出下面代码分别输出什么
'''
class A(object):
    x=1
class B(A):
    pass
class C(A):
    pass
print(A.x,B.x,C.x)
'''1 , 1  , 1 '''
B.x=2
print(A.x,B.x,C.x)
'''1,2,1 '''
C.x=2
print(A.x,B.x,C.x)
'''1,2,2 '''













