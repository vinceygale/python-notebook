# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 13:18:48 2021

@author: vincey
"""
import pyinputplus as pyip
import random
import time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = '# %s: %s x %s = ' % (questionNumber, num1, num2)
    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1*num2)],
                      blockRegexes=[('.*', 'Incorrect!')],
                      timeout=8, limit=4)
    except pyip.TimeoutException:
        print('Out of time!!!')
    except pyip.RetryLimitException:
        print('Out of tries!!!')
    else:
        print('Correct!')
        correctAnswers += 1
        time.sleep(2)
    print('Score: %s / %s' % (correctAnswers, numberOfQuestions))
