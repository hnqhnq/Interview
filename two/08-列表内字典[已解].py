""" 
@file: 08-列表内字典[已解].py
@Time: 2018/07/29
@Author:heningqiu
"""
'''
按accuracy_rate字段数值大小升序排序（accuracy_rate相等时安装value降序排序）
'''
data=[
    {"name":"Linux","value":12,"accuracy_rate":"44"},
    {"name":"Windows","value":21,"accuracy_rate":"76"},
    {"name":"IOS","value":60,"accuracy_rate":"44"},
    {"name":"Android","value":8,"accuracy_rate":"90"},
    {"name":"OS X","value":32,"accuracy_rate":"90"},
]


# for i in range(len(data)):
#     sorted(data,key=lambda i:int(data[i]['accuracy_rate']))
#     for j in range(len(data)-i):
#         if data[i]['accuracy_rate']==data[j]['accuracy_rate']:
#             sorted(data,key=lambda j:int(data[j]['value']))

a=sorted(data,key=lambda s:int(s['accuracy_rate']),reverse=False)
print(a)
print("******")
print(sorted( data,key = lambda x:(int(x["accuracy_rate"]),-x["value"])))

