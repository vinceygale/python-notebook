# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 09:54:19 2021

@author: vincey
"""
#!python 3
#一个疯狂填词程序，读入文件后请求新数据并重新生成新文件。        
 
#import sys,shelve,pyperclip
LINE='\n------------------------------\n'
LIST=[{'ADJECTIVE':''},{'NOUN':''},{'VERB':''},{'NOUN':''},{'FLAG':True}]


def askInput():
    LIST[0]['ADJECTIVE']=input('Enter an adjective:')
    LIST[1]['NOUN']=input('Enter a noun:')
    LIST[2]['VERB']=input('Enter a verb:')
    LIST[3]['NOUN']=input('Enter a noun:')
    flag=input("Enter any words to continue or \'exit\' to exit :")
    if flag=='exit':
        LIST[4]['FLAG']=False

print(LINE+'程序将找到这些出现的单词，并提示用户取代它们'+LINE)
tmp=open('readme.txt','a+')
tmp.seek(0)
txt=tmp.read()
while LIST[4]['FLAG']:
    askInput()
    tmp.seek(2)
    tmp.writelines('The '+LIST[0]['ADJECTIVE']+ ' panda walked to the '+
               LIST[1]['NOUN']+' and then '+LIST[2]['VERB']+'. A nearby '+
               LIST[3]['NOUN']+' was unaffected by these events.')
tmp.seek(0)
print(tmp.read())
tmp.close()
