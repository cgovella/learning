# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 15:16:33 2017

@author: chris
"""
import random

def password(length):
    pw = str()
    characters = "abcdef"
    for i in range(length):
        pw = pw + random.choice(characters)
    return pw