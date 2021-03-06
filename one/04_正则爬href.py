""" 
@file: 04_正则爬href.py
@Time: 2018/07/22
@Author:heningqiu
"""
import re

'''9.用python抓取一个网页（例如：www.qq.com），用正则匹配页面的所有链接'''
# 2.根据需求构建好链接提取的正则表达式
pattern1 = '<.*?href="(.*?)">'
b='<link rel="canonical" href="https://blog.csdn.net/IT_zxl001/article/details/80027845">'
print(re.findall(pattern1,b)) #
'''['https://blog.csdn.net/IT_zxl001/article/details/80027845']'''

import urllib.request
import re

# 1. 确定好要爬取的入口链接
url = "http://www.qq.com/"
# 2.根据需求构建好链接提取的正则表达式
# pattern1 = '<.*?(href=".*?").*?'
# 3.模拟成浏览器并爬取对应的网页 谷歌浏览器
headers = {'User-Agent':
           'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read().decode('utf8')
# 4.根据2中规则提取出该网页中包含的链接
content_href = re.findall(pattern1, data, re.I)
# print(content_href)
# 5.过滤掉重复的链接
#    # 列表转集合(去重) list1 = [6, 7, 7, 8, 8, 9] set(list1) {6, 7, 8, 9}
set1 = set(content_href)
# 6.后续操作，比如打印出来或者保存到文件中。
file_new = "./href.txt"
with open(file_new, 'w') as f:
    for i in set1:
        f.write(i)
        f.write("\n")
# f.close()
print('已经生成文件')



