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
    neg, pos, zero = 0, 0, 0
    for numb in arr:
        if numb < 0:
            neg += 1
        elif numb > 0:
            pos += 1
        else:
            zero += 1
    print(f"{pos / len(arr):6f}\n{neg / len(arr):6f}\n{zero / len(arr):6f}")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
