#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    print(f'{sum(y>0 for y in arr)/len(arr):.06f}')
    print(f'{sum(y<0 for y in arr)/len(arr):.06f}')
    print(f'{sum(y==0 for y in arr)/len(arr):.06f}')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
