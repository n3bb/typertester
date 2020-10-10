#!/bin/env python3
# Typertester - command line typing training!

import getpass 
import sys
import config
import random
import difflib
import time

DICT = config.dict
SPRINT_LEN = config.sprintLen
TEXT_INVISIBLE = config.textInvisible
Sentence = []

def getDiff(cases):
    # Takes list of tuples containing two strings, returns parse-able diff 
    add = []
    remove = []
    for a,b in cases:
    #print('{} => {}'.format(a,b))  
        for i,s in enumerate(difflib.ndiff(a, b)):
            if s[0]==' ': continue
            elif s[0]=='-':
            	    #print(u'Delete "{}" from position {}'.format(s[-1],i))
                remove.append(("-"+s[-1], i))
            elif s[0]=='+':
            			#print(u'Add "{}" to position {}'.format(s[-1],i))
                add.append(("+"+s[-1], i))
    return remove, add

def getIncorrectChars(diff):
    final = []
    for x in range(len(diff)): 
        for i in range(len(diff[x])): 
            if diff[x][i][0][0] != "-":
                final.append(diff[x][i][0][1:])
    return final

def getWPM(deltatime, words: int = SPRINT_LEN):
    return (words / deltatime) * 60
    

while True:
    Sentence = []
    for x in range(SPRINT_LEN):
        Sentence.append(random.choice(DICT).lower())

    Sentence = " ".join(Sentence)

    print(Sentence)

    if TEXT_INVISIBLE:
        start = time.perf_counter()
        Text = getpass.getpass("")
    else:
        start = time.perf_counter()
        Text = input()

    print(''.join(getIncorrectChars(getDiff([(Text, Sentence)]))),f"{getWPM(time.perf_counter()-start):0.1f}")
    
