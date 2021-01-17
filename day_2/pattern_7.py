"""
n = 5
   0 1 2 3 4
0: 1
1: 1 2
2: 1 2 3
3: 1 2 3 4
4: 1 2 3 4 5

# increasing numbers
count = i + 1

i j
f(i, j) = j + 1

# new line
"""

"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""



# for i in range(n):
#     # 1 + 2 + 3 + 4 + 5 + .... + n = n(n + 1) /2 == n^2/2 = O(n^2)
#     # increasing numbers
#     # time Complexity: O(i)
#     for j in range(i + 1):
#         print(j + 1, end=' ')
#
#     # new line
#     print()


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

n = int(input())
row = '1 '
for i in range(n):
    # iteration: O(1)
    print(row)
    row += f'{i + 2} '
