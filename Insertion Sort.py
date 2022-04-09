#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    temp=arr[-1]
    
        
                
    for i in range(2,n+1):
        
        if temp < arr[-i]:
            if i==n and arr[-n]>temp:
                arr[-i+1]=arr[-i]
                for i in arr:
                    print(i,end=" ")
                print()
                arr[-i]=temp
                for i in arr:
                    print(i,end=" ")
                
                continue
            arr[-i+1]=arr[-i]
            for i in arr:
                print(i,end=" ")
            print()
        else :
            if arr[0]>temp:
                arr[0]=temp
            else :
                arr[-i+1]=temp
            
            for i in arr:
                print(i,end=" ")
            print()
            break
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
