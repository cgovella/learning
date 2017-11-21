#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 17:36:59 2017

@author: chris
"""

def read_seq(inputfile):
    """ Reads and returns the input sequence with special characters removed
    """
    with open(inputfile, "r") as f:
        seq = f.read()
    seq = seq.replace("\n", "")
    seq = seq.replace("\r", "")
    return seq 

        


inputfile = "dna.txt"
with open(inputfile, "r") as f:
    seq = f.read()






inputfile = "dna.txt"
f = open(inputfile, "r")
seq = f.read()
seq = seq.replace("\n", "")
seq = seq.replace("\r", "")

def translate(seq):
    """
    translate takes a string, containing a nucleotide sequence, splits it into
    a range of three, then crossreferences it against a table of amino acids.
    """
    table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    # check that the seq is divisble by 3
    protein = "" 
    if len(seq) % 3 == 0: 
        for i in range(0, len(seq), 3): # loop over
            codon = seq[i:i+3] # extract a single codon
            protein += table[codon] # look it up from table[] and add it to protein
        return protein