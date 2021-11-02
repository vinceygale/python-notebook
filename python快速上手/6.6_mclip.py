# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 09:16:03 2021

@author: vincey
"""
import sys
import pyperclip
LINE = '\n------------------------------------\n'
TEXT = {'agree': """Yes,i agree. That sounds fine to me.""",
        'busy': """Sorry,can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""
        }
print(LINE)
if len(sys.argv) < 2:
    print('Usage:py mclip.py [keyphrase]  - copy phrase text')
    sys.exit()
keyphrase = sys.argv[1]
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for '+keyphrase+' copied to clipboard.')
else:
    print('There is no text for '+keyphrase)

print(LINE)
