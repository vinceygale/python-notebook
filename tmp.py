# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 09:54:19 2021

@author: vincey
"""
#!python 3

#功能：把文件名中含有的MM－DD－YYYY转换成DD－MM－YYYY      
 
import shutil,re,os

dateRe=re.compile(
    r"""(.*)?                       #文件名前边的字符
    ([0][1-9]-|[1][0-2]-)           #匹配月份
    ([0-2]\d-|[3][0-1]\d-)          #匹配日期
    ([19|20]\d*)                    #匹配年份
    (.*)?                           #匹配文件后面的字符
    """,
    re.VERBOSE
    )


myPath='test'
homePath=os.path.abspath(myPath)

# =============================================================================
# 只能修改本文件夹下的文件
#
# for fileName in os.listdir(homePath):
#     match=dateRe.search(fileName)
#     if match is not None:
#         day=match.group(3)
#         month=match.group(2)
#         oldStr=str(month+day)
#         newStr=str(day+month)
#         print('Old file name is : '+fileName)
#         newFileName=fileName.replace(oldStr, newStr)
#         print('New file name is : '+newFileName)
#         shutil.move(fileName, newFileName)
# #print(os.listdir(homePath))
# print('文件更名完成!!!')
# 
# =============================================================================
#print(os.path.basename(homePath))

# =============================================================================
# 可以修改目录树下所有匹配上的文件名
# 
# for path,subPaths,fileNames in os.walk(homePath):
#     for fileName in fileNames:
#         workPath=os.path.join(path, fileName)
#         match=dateRe.search(workPath)
#         if match is not None:
#             day=match.group(3)
#             month=match.group(2)
#             oldStr=str(month+day)
#             newStr=str(day+month)
#             print('Old file name is : '+workPath)
#             newFileName=os.path.join(path,fileName.replace(oldStr, newStr))
#             print('New file name is : '+newFileName)
#             shutil.move(workPath, newFileName)
# print('文件更名完成!!!')
#  
# =============================================================================
