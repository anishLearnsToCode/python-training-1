"""
Time Complexity: O(1)
Space Complexity: O(1)
"""

i = 0
while i < 4:
    j = 0
    while j < 3:
        print(i + j)
        j = j + 1
    i = i + 1

print(i + j)

"""
Output
i = 4
j = 3
0
1
2
1
2
3
2
3
4
3
4
5
7
"""