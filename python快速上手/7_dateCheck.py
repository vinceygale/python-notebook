# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 12:54:42 2021

@author: vincey
"""

# To Check the datetime like 'DD/MM/YYYY'

import re

dateRegex = re.compile(r'^([012]\d|30|31)/(0\d|10|11|12)/([12]\d{3})$')
date = {'day': '', 'month': '', 'year': ''}


dateTime = '31/06/2200'

# 检查年份是否是润年


def checkRN(year: int):
    if year % 4 != 0:
        return False
    elif year % 400 != 0:
        return False
    else:
        return True

# 检查月份与日期是否正确


def checkMD(month: int, day: int):
    if month == 0 or day == 0:
        return False
    if day == 31 and month in [4, 6, 9, 11]:
        return False
    return True


# 校验日期格式是否正确
def checkDate(datetime: str):  # datetime must like 'DD/MM/YYYY'
    if re.search(dateRegex, datetime) is not None:
        return True
    else:
        return False


# 检验主函数
def checker(datetime: str):
    if not checkDate(datetime):
        print(datetime+' is not a right format of datetime!!!')
    else:
        lst = datetime.split('/')
        date['day'] = lst[0]
        date['month'] = lst[1]
        date['year'] = lst[2]

        if not checkMD(int(date['month']), int(date['day'])):
            print('Please check the ' +
                  date['day']+' of the '+date['month'])
        elif date['month'] == 2 and date['day'] >= 29 and not checkRN(int(date['year'])):
            print('Does Febroriay has ' +
                  date['day']+'days in '+date['year']+' ?')
        else:
            print(dateTime + ' is the rigtht date format!')


# consle 界面交互输入
dateTime = input('Input a datetime like "DD/MM/YYYY" or quit with Q :')
while(dateTime is not None):
    if dateTime != 'Q':
        checker(dateTime)
        dateTime = input(
            'Input a datetime like "DD/MM/YYYY" or quit with Q :')
    else:
        break
