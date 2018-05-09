# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 08:51:26 2016

@author: Tobias Gretenkort
"""

#Language Inventor Debugged Version & Repetition Avoid. ##### The part that avoids repetition is in def newWords():

#section I 10-14:  import of modules and setting of working directory
import random
import os
import re
os.chdir('C:\\Program Files\\python35')
 
vowels = ['a','e','i','o','u']
consonants = ['k','s','t', 'n','h','m','y','r','w','g','z','d','b','p']
syllables = []
FakeWords = []
doubledwords = []
WordList = []

def new_syllables():
    for i in consonants:
        c = i 
        for i in vowels: 
            new_syllable = c + i 
            syllables.append(new_syllable)
    syllables.remove('bu')
    syllables.remove('so')
    syllables.remove('na') 
    syllables.remove('te')

def twosyllableWord():   
    new_two_syllable_Word = random.choice(syllables) + random.choice(syllables) 
    return new_two_syllable_Word  
    
def threesyllableWord():   
    new_three_syllable_Word = random.choice(syllables) + random.choice(syllables) + random.choice(syllables)
    return new_three_syllable_Word
    
def choose_txt():
    print('Which file would you like to open?')
    while True:        
        Wordfile = input()  
        try:                    
            text = open(Wordfile).read()
            WordList = text.split()
        except OSError:
            print('There is no such file.')
            break
            choose_txt()
    print('These are the words contained in the list you opened')
    print(WordList)
    
def manual_input():
    print('Input all the words you want to translate. When you are finished, type "exit"')
    while True:   
        word = input()
        word = word.lower()
        if word == 'exit':
            break 
        else:
            WordList.append(word)
            print('These are the words you chose to translate into the fake language.')
            print(WordList)         

def new_word():
    global newWord
    newWord = random.choice([twosyllableWord(), twosyllableWord(), threesyllableWord()]) #I added the twosyllableWord() function again to have a 2/3 vs 1/3 weighted choice, so that more of the words in the fake language are short words and not long words (to prevent grounding effect in the experiment, due to language difficulty)        
    FakeWords.append(newWord)            
    doubledwords.append(newWord)
    
def newWords():   
    while not len(WordList) == len(FakeWords):    
        new_word()   
        double_check()
                
def double_check():
    with open("doubledwords.txt", "a") as mf:
        for w in FakeWords:
            indexRegex = (re.compile(' '.join(doubledwords)))
            result = indexRegex.findall(' '.join(open("doubledwords.txt").read()))           
            if not result == []:
                FakeWords.remove(newWord)
                doubledwords.remove(newWord)
            else:
                print(newWord, " ", file = mf)
            
def storeDict():
    print('These are the new correspondant words for your worlist No')
    print(FakeWords)
    FakeDictionary = dict(zip(WordList, FakeWords))
    try: 
        with open ("counterfile", "r") as f:
            filenum = int(f.read())
    except (IOError, ValueError):
        filenum = 1
    with open("counterfile", "w") as f:
        f.write(str(filenum + 1))
    filename = "LanguageDictionary%s.txt" % filenum
    with open(filename, "w") as f:
        for k, v in FakeDictionary.items(): 
            left = max((len(i) for i in FakeDictionary))
            right = max((len(i) for i in FakeDictionary))
            print(k.ljust(left + 5, '-') + v.rjust(right + 5, '-') + "\n", file=f)
    FakeWords.clear()


print('Welcome to the language inventor. This program can make up random words')
print('for a ficticious language. You just need to define which words you want')
print('to translate into your new fake language. Do you want to import words')
print('from a text file (type "txt") or store them in the program manually')
print('(type "manual")')
while True:
    choice = input() 
    if choice == 'manual':
        manual_input() 
        break
    if choice == 'txt':
        choose_txt()
        break
    else:
        print('type "manual" or "txt"')
print('How many versions of the language do you need?')
while True:    
    try:
        number = int(input())
        break
    except ValueError:
        print('I only accept numbers!')
for _ in range(number): 
    new_syllables()
    newWords()
    storeDict()
   
