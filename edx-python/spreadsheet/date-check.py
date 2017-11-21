#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 11:40:45 2017

@author: chris
"""


#text = "This is my test text. We're keeping this short to keep things manageable."
#
#def count_words(text):
#    """
#    Count the number of times a word occurs in str. Skip punctuation.
#    """
#    text = text.lower()
#    skips = [".", ",", ";", ":", "'", '"']
#    for ch in skips:
#        text = text.replace(ch, "")
#        
#    word_counts = {}
#    for word in text.split(" "):
#        # known word
#        if word in word_counts:
#            word_counts[word] += 1
#        # unknown word
#        else:
#            word_counts[word] = 1
#    return word_counts
        
import csv
# open a spreadsheet
table = open('old-transactions-gpwa.csv')
tableReader = csv.reader(table)
tableData = list(tableReader)

memberjoin = []
# look at the first column and iterate down each cell in that column
# take the value and check
for row in tableData:
    name = row[0]
    date = row[4]
    if name in memberjoin:
        memberjoin[memberjoin.index(name)]
    else:
        memberjoin.append(name)
        
# if it exists, append a new value to the 2nd lsit
# if it is new, create a second list with the value stored in the next cell as the first value
# return the list