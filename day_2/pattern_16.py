"""
n = 4
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

count: i + 1
f(i, j) = i (i + 1) / 2 + 1 + j
1 + 2 + 3 + 4 + ... + n = n (n + 1) / 2
"""

n = int(input())
# k = 1

# for i in range(n):
#     for _ in range(i + 1):
#         print(k, end=' ')
#         k += 1
#     print()


for i in range(n):
    for j in range(i + 1):
        print(i * (i + 1) // 2 + 1 + j, end=' ')
    print()
