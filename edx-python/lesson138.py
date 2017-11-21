# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def intersect(s1, s2):
    res = []
    for x in s1:
        if x in s2:
            res.append(x)
    return res