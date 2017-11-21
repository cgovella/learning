#! /bin/env python3
''' Functional wrapper around the bitwise operators.
Designed to make their use more intuitive to users not
familiar with the underlying C operators.
Extends the functionality with bitmask read/set operations.

The inputs are integer values and
return types are 16 bit integers or boolean.
bit indexes are zero based

Functions implemented are:
    NOT(int)           -> int
    AND(int, int)      -> int
    OR(int,int)        -> int
    XOR(int, int)      -> int
    shiftleft(int, num)  -> int
    shiftright(int, num) -> int
    bit(int,index)     -> bool
    setbit(int, index) -> int
    zerobit(int,index) -> int    
    listbits(int,num) -> [int,int...,int]
'''

def NOT(value):
    return ~value

def AND(val1,val2):
    return val1 & val2

def OR(val1, val2):
    return val1 | val2

def XOR(val1,val2):
    return val1^val2

def shiftleft(val, num):
    return val << num

def shiftright(val, num):
    return val >> num

def bit(val,idx):
    mask = 1 << idx    # all 0 except idx
    return bool(val & mask)

def setbit(val,idx):
    mask = 1 << idx    # all 0 except idx
    return val | mask

def zerobit(val, idx):
    mask = ~(1 << idx)   # all 1 except idx
    return val & mask
    
def listbits(val):
    num = len(bin(val)) - 2
    result = []
    for n in range(num):
        result.append( 1 if bit(val,n) else 0 )
    return list( reversed(result) )
 
