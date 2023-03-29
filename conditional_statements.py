#!/bin/python3
#n odd --> weird | n even within 2-5 not weird | n even 6-20 weird| n even > 20 not weird
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
if N % 2 != 0  :
    print("Weird")
elif (N%2==0 and N in range(2,6)):
    print("Not Weird")
elif (N%2==0 and N in range(6,21)):
    print ("Weird")
elif (N%2==0 and N > 20 ):
    print("Not Weird")
