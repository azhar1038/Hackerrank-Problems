#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPower' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def maximumPower(s):
    # Write your code here
    max_len=0
    for i, c in enumerate(s):
        if c=='1':
            s=s[i:]+s[:i]
            break
    i=0
    while i<len(s):
        current_len=0
        if s[i]=='1':
            i+=1
        else:
            while i<len(s) and s[i]=='0':
                current_len += 1
                i+=1
        if current_len > max_len:
            max_len = current_len
    if max_len == len(s):
        return -1

    return max_len
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = maximumPower(s)

    fptr.write(str(result) + '\n')

    fptr.close()
