""" 
@file: 05-星代表的含义.py
@Time: 2018/07/29
@Author:heningqiu
"""
'''
7.解释下列情况中，*各代表什么含义？
①def fun(*args,**kwargs):
    pass
*代表不定长位置参数
**代表不定长关键字参数

②_,*r,_ =range(100) ： 
*代表1-98之间所有的值
举栗子：
_,*q,_,_=range(10)
print(q)  # [1, 2, 3, 4, 5, 6, 7]

③fun(*a) *代表向函数传入一个不定长的列表或者元组
④fun(a,**b) ** 代表向函数传入一个不定长的字典
⑤fun(a**b) ** 代表 a的b次方算术
'''
def fun(*args,**kwargs):
    pass

_,*r,_ =range(100)
print(_,r,_)

print(range(100))
print(round(1.5))

_,*q,_,_=range(10)
print(q)  # [1, 2, 3, 4, 5, 6, 7]

a=[1,2,3]
b={1:99,2:100}
fun(*a)
fun(a,**b)
fun(a**b)