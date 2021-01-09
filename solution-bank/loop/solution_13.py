"""
WAP to print Fibonacci series of n terms where n is input by user : 1 1 2 3 5 8 13 24 .....
"""

n = int(input())

previous = 0
current = 1
for i in range(n):
    print(current, end=' ')
    current, previous = current + previous, current
