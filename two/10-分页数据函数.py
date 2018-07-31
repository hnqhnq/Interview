""" 
@file: 10-分页数据函数.py
@Time: 2018/07/29
@Author:heningqiu
"""

import pymysql

def get_data(page_now,page_size,limit_start,db=pymysql):
    conn=pymysql.connect(host='127.0.0.1', user='root', password="7880660",
                 database='Interview', port=3306, charset='utf8')
    cursor=conn.cursor()
    cursor.execute('select name,value from paging ')
    ret= cursor.fetchall()
    print(ret)
    cursor.close()
    conn.close()
'''  --------------------------          '''


def get_page(m, n):
    cur_page = n
    pages = []

    if cur_page <= 6:  # 百度分页为例
        limit_start = 1  # 起始页
    else:
        limit_start = cur_page - 5

    if m >= cur_page + 4:

        if cur_page < 6:
            limit_end = m - limit_start
        else:
            limit_end = cur_page + 4

    else:
        limit_end = m
        if cur_page >= 10:
            limit_start = limit_end - 9

    for i in range(limit_start, limit_end + 1):  # 这才是分页的关键

        if cur_page == i:
            pages.append(cur_page)
        else:
            pages.append(i)

    return pages

# PER_PRE_NUM = 6
# PER_NUMBER_MAX = 10
# def get_page(m, n):
#     cur_page = n
#     limit_start = 1 if cur_page <= PER_PRE_NUM else cur_page - (PER_PRE_NUM - 1)
#     if m >= cur_page + (PER_PRE_NUM - 2):
#         limit_end = m - limit_start if cur_page < PER_PRE_NUM else cur_page + (PER_PRE_NUM - 2)
#     else:
#         limit_end = m
#         if cur_page >= PER_NUMBER_MAX:
#             limit_start = limit_end - (PER_NUMBER_MAX - 1)
#     return [i for i in xrange(limit_start, limit_end + 1)]


if __name__ == '__main__':
    # get_data()
    get_page(10,6)




