""" 
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example

The minimum sum is  and the maximum sum is . The function prints

16 24
Function Description

Complete the miniMaxSum function in the editor below.

miniMaxSum has the following parameter(s):

arr: an array of  integers
Print

Print two space-separated integers on one line: the minimum sum and the maximum sum of 4 of 5 elements.
"""

def miniMaxSum(arr):
    min_res = 0
    max_res = 0
    
    for i in range(len(arr)):
        if arr[i] == min(arr) or arr[i] < max(arr):
            min_res += arr[i]
        if arr[i] == max(arr) or arr[i] > min(arr):
            max_res += arr[i]
    
    print(min_res, max_res)
    
## fails on [5,5,5,5,5] (all elements are the same)

def miniMaxSum(arr):
    min_res = 0
    max_res = 0
    
    for i in range(len(arr)):
        if arr[i] <= max(arr):
            min_res += arr[i]
        if arr[i] >= min(arr):
            max_res += arr[i]
            
        
    min_res -= max(arr)
    max_res -= min(arr)
    print(min_res, max_res)

## better approach:

def miniMaxSum(arr):
    min_res = sum(arr) - max(arr) # Minimum Total means sum of all numbers minus largest number
    max_res = sum(arr) - min(arr) # Maximum Total means sum of all numbers minus smallest number
    
    print(min_res, max_res)