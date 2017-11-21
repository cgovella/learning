# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def word_stats(word_counts):
    """Return number of unique words and word requencies."""
    
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)