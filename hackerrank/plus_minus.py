""" 
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

Example

There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:

0.400000
0.400000
0.200000
Function Description

Complete the plusMinus function in the editor below.

plusMinus has the following parameter(s):

int arr[n]: an array of integers
Print
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.

Input Format

The first line contains an integer, n, the size of the array.
The second line contains n space-separated integers
"""

def plusMinus(arr):
    if len(arr) <= 0:
        return 0
        
    zero_count = 0
    positive_count = 0
    negative_count = 0
    for num in arr:
        if num == 0:
            zero_count += 1
        elif num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
    
    print(round(positive_count/len(arr), 6))
    print(round(negative_count/len(arr), 6))
    print(round(zero_count/len(arr), 6))