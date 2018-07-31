""" 
@file: test.py
@Time: 2018/07/22
@Author:heningqiu
"""

# dict = {"system": "系统", "China": "中国", "link": "联接"}
#
# x = input("请输入一个英文单词：")
# print(dict.get(x, "本字典里没找到!"))


def deco(greetings):
    def wrapper(*args, **kwargs):
        msg = greetings(*args, **kwargs)
        ret = msg[0].upper() + msg[1:]
        return ret
    return wrapper

@deco
def greetings(word="hi there"):
    return word.lower()

print(greetings())


def add(x, y):
    return x + y


add1 = lambda x, y: x + y
print(add(1,2))

print("--------------------")
a=set([1,2,3])
b=set([2,3,4])
print(a)
print(b)
print(a&b)
print(a|b)

print("--------------------")
def sum(n):
    if n<0:
        return 0
    else:
        return n+sum(n-1)

print(sum(2))


list_b=[12,213,22,2,2,2,22,2,2,32]
print([list_b[i] for i in list(filter(lambda x:x,[i for i in range(len(list_b))]))])


#
# sum1=filter(lambda s:s+sum1(s-1),[s for s ])
#
# print(sum1(2))


for i in range(1,10,5):
    print(i)

print("*"*30)

coun=1
def ff():
    # coun = 1
    global coun
    for i in (1,2,3):
    # for i in range(3):
        print('wh?',i)
        coun+=1
ff()
print(coun,'haha')

a=[1,2,3,4,5,6,7,8,9,10]
print(a[::3]) #[1, 4, 7, 10]
print(a[-2:]) #[9, 10]

print("--------------------")

def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)
f(2) #[0, 1]
f(3,[3,2,1]) #[3, 2, 1, 0, 1, 4]
f(3) #[0, 1, 0, 1, 4]
f(4) #[0, 1, 0, 1, 4, 0, 1, 4, 9]
print("--------------------")
a=[]
def fun(a):
    a.append(1)

fun(a)
print(a)