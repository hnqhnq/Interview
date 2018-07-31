""" 
@file: 01-字符串分割拼接.py
@Time: 2018/07/28
@Author:heningqiu
"""




# print(len(one))
# print(one[0:2])
# print(one[2:4])
# print(one[4:6])
one="ab&&2"
lst=[]
for i in range(0,len(one),2):
    if one[i:i+2]!="&&":
        print(one[i:i+2])
        lst.append(one[i:i+2])
print(lst)

two=["ab","2"]
str1=""
for i in two:
    str1+=i+"&&"
print(str1[:-2])
