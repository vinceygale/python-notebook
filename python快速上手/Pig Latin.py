# -*- coding: utf-8 -*-
"""
Pig Latin Game

Created on Thu Sep 23 13:40:27 2021

@author: vincey
"""
LINE = '-'*40
VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']


def checkWords(word: str):  # 检测字符性质
    myWord = ''
    if word[0].isnumeric():
        myWord = word
    elif word.lower()[0] in VOWELS:
        myWord = startWithVowel(word)
    else:
        myWord = startWithConsonant(word)
    return myWord


def startWithConsonant(word: str):  # 处理辅音开头的字符
    myChars = ''
    titleFlag = word.istitle()
    upperFlag = word.isupper()
    word = word.lower()
    while len(word) > 0 and word[0] not in VOWELS:
        myChars += word[0]
        word = word[1:]
    word = word+myChars+'ay'
    if(titleFlag):
        word = word.title()
    if(upperFlag):
        word = word.upper()
    return word


def startWithVowel(word: str):   # 处理元音开始的字符
    myChars = word+'yay'
    if word.istitle():
        myChars = myChars.title()
    if word.isupper():
        myChars = myChars.upper()
    return myChars


print(LINE)
print('Enter the English message to translate into Pig Latin:')
msg = input()
newWords = []
words = msg.split()
for i in range(len(words)):
    # print(words[i])
    newWords.append(checkWords(words[i]))
print(' '.join(newWords))
