#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
class Item:
    def __init__(self, value, repeat):
        self.value = value
        self.repeat = repeat
        self.index = 1
    def __str__(self):
        return f"({self.value}, {self.repeat}, {self.index})"

def beautifulTriplets(d, arr):
    count=0
    l = []
    i=0
    while i < len(arr):
        j=i
        repeat=0
        while arr[i] == arr[j]:
            repeat += 1
            j += 1
            if j == len(arr):
                break
        i = j
        item = Item(arr[i-1], repeat)
        while len(l):
            if l[0].value + d < item.value:
                l.pop(0)
            else:
                break
        if len(l) == 0:
            l.append(item)
        elif l[0].value + d == item.value:
            oldItem = l.pop(0)
            item.index = oldItem.index + 1
            item.repeat *= oldItem.repeat
            print('Appending', item)
            l.append(item)
            if item.index > 2:
                count += item.repeat
                print('Modified Count', count)
        else:
            l.append(item)
        print_list(l)
    return count

def print_list(l):
    print('\n[')
    for i in l:
        print(i)
    print(']\n')

# arr = [1, 6, 7, 7, 8, 10, 12, 13, 14, 19]
arr = [1,1,1,2,4,4,4,5,7,7,7,8]
print(beautifulTriplets(3, arr))