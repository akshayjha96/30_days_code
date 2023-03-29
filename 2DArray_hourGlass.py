#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    
    def get_hour_glass_sum(matrix,row,col):
        total_sum = matrix[row][col]
        total_sum += matrix[row-1][col-1]
        total_sum += matrix[row-1][col]
        total_sum += matrix[row-1][col+1]
        total_sum += matrix[row+1][col-1]
        total_sum += matrix[row+1][col]
        total_sum += matrix[row+1][col+1]
        return total_sum
        

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    max_hourglass_sum = -63 #(minimum possible value of all the sums)
    for i in range(1,5):
        for j in range(1,5):
            current_hourglass_sum = get_hour_glass_sum(arr,i,j)
            if current_hourglass_sum > max_hourglass_sum:
                max_hourglass_sum = current_hourglass_sum
    
    print(max_hourglass_sum)
    
