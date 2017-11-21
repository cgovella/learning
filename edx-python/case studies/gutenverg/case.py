#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 14:03:28 2017

@author: chris
"""

text = "This is my test text. We're keeping this short to keep things manageable."

def count_words(text):
    """
    Count the number of times a word occurs in str. Skip punctuation.
    """
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")
        
    word_counts = {}
    for word in text.split(" "):
        # known word
        if word in word_counts:
            word_counts[word] += 1
        # unknown word
        else:
            word_counts[word] = 1
    return word_counts
        
from collections import Counter
def count_words_fast(text):
    """
    Count the number of times a word occurs in str. Skip punctuation.
    """
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")
        
    word_counts = Counter(text.split(" "))
    return word_counts

def read_book(title_path):
    """
    Read a book and return it as a string.
    """
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text

def word_stats(word_counts):
    """Takes a specific word_counts object. Return number of unique words and word requencies."""
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)



text = read_book("./Books/English/shakespeare/Romeo and Juliet.txt")
word_counts = count_words(text)
(num_unique, counts) = word_stats(word_counts)
print(num_unique, sum(counts))






import os
book_dir = "./Books"
import pandas as pd
#table known as dataframe
stats = pd.DataFrame(columns = ("language", "author", "title", "length", "unique"))
title_num = 1
#table.loc[1] = "James", 22
#table.loc[2] = "Jess", 32
#table
#table.columns
#os.listdir(book_dir) # returns a list

import os
book_dir = "./Books"

import pandas as pd
stats = pd.DataFrame(columns = ("language", "author", "title", "length", "unique"))
title_num = 1

for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + language): # from the outer loop
        for title in os.listdir(book_dir + "/" + language + "/" + author):
            inputfile = book_dir + "/" + language + "/" + author + "/" + title
            print(inputfile)
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words(text))
            stats.loc[title_num] = language, author.capitalize(), title.replace(".txt", ""), sum(counts), num_unique
            title_num += 1

## video 3.2.6

 

        
## example table
import pandas as pd
#table known as dataframe
table = pd.DataFrame(columns = ("name", "age"))
table.loc[1] = "James", 22
table.loc[2] = "Jess", 32
table
table.columns




























