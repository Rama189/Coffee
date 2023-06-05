from os import *
from sys import *
from collections import *
from math import *
#https://www.codingninjas.com/codestudio/problems/ceiling-in-a-sorted-array_1825401?leftPanelTab=0
def ceilingInSortedArray(n, x, arr):
    l = 0
    h = len(arr) - 1
    res = -1
    if x <= arr[l]:
        return arr[l]
    while l <= h:
        mid = l + h - l // 2
        if arr[mid] == x:
            res = arr[mid]
            break
        elif arr[mid] < x:
            l = mid + 1
        elif arr[mid] > x:
            h = mid - 1
            if res == -1:
                res = arr[mid]
            elif arr[mid] < res:
                res = arr[mid]
    return res
    # Write your code here.
