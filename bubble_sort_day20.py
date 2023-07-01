#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    totalnumberofswaps = 0
    
    for i in range(n):
        numswaps = 0
        for j in range(n-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                
                numswaps += 1
        totalnumberofswaps += numswaps
        
        if numswaps == 0:
            break
        
    print('Array is sorted in ' + str(totalnumberofswaps) + " swaps.")
    print("First Element: "+str(a[0]))
    print("Last Element: "+str(a[-1]))
    
