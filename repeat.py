#!/usr/bin/python

import sys

def repeat (word, exc):
    ret = word * 3
    if exc:
        ret += '!!!'
    return ret

print repeat('Yay', False)
print repeat('Woo Hoo', True)
