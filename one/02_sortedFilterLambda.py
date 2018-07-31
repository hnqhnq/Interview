""" 
@file: 02_sortedFilterLambda.py
@Time: 2018/07/22
@Author:heningqiu
"""
'''
5.通过sorted函数或者列表的sort函数和lambda对下面的列表按score排序
'''
''' 总结：
    sorted()函数是可迭代对象，参数：key、reverse
    key : 按哪个元素进行排序，可配合隐函数lambda
    reverse=True 是降序
    列表包含字典的取值：list_a[0]['name'] / list_a[0]['score']
 '''
list_a=[
    {"name":"p1","score":100},
    {"name":"p2","score":10},
    {"name":"p3","score":30},
    {"name":"p4","score":20},
    {"name":"p5","score":80},
    {"name":"p6","score":70},
    {"name":"p7","score":60},
    {"name":"p8","score":40},
    ]
a=sorted(list_a,key=lambda s:s['score'],reverse=True)
print(a)

print("-------------我是分割线--------------")
'''6.一行代码，通过filter和lambda函数输出以下列表索引为奇数对应的元素，
 list_b=[12,213,22,2,2,2,22,2,2,32]
 '''
'''总结：
filter：过滤  、  lambda：隐函数lambda s:s%2==0
ilter(function or None, sequence) -> list, tuple, or string
第一个参数为None的情形:
filter(None, '101') # '101'
filter(None, [True,False]) #[True]
第一个参数为function的情形:【结合lambda做过滤】
list(filter(lambda x: x, [-1, 0, 1])) #[-1, 1]
list(filter(lambda x: not x, [-1, 0, 1])) #[0]
'''
list_b=[12,213,22,2,2,2,22,2,2,32]
print([list_b[i] for i in list(filter(lambda x:x%2==1,[i for i in range(len(list_b))]))])

print("-------------我是分割线---test-----------")
print(list(filter(lambda x:x%2==1,[x for x in range(10)])))
print(list(filter(lambda x:not x%2,[x for x in range(10)])))
print(list(filter(lambda x:x%2,[x for x in range(10)])))
'''代码的意思是输出 555555 最大的三位数的约数是多少'''
print(max(filter(lambda x: 555555 % x == 0, range(100, 999))))

print("-------------我是分割线--------------")





