"""
SPOJ - PRIME GENERATOR

Peter wants to generate some prime numbers for his cryptosystem. Help him! Your task is to generate all prime numbers between two given numbers!

Input
The input begins with the number t of test cases in a single line (t<=10). In each of the next t lines there are two numbers m and n (1 <= m <= n <= 1000000000, n-m<=100000) separated by a space.

Output
For every test case print all prime numbers p such that m <= p <= n, one number per line, test cases separated by an empty line.

Input:
2
1 10
3 5

Output:
2
3
5
7

3
5
 
"""


def prime_generator(arr):
    lower = arr[0]
    upper = arr[1]
    
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

test_count = int(input())
while test_count != 0:
    number_test = input()
    num_range = list(map(int, number_test.split()))
    prime_generator(num_range)
    test_count -= 1
                    

    