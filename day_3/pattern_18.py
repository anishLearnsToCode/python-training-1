from day_3.combinatorics import combination

"""
n = 5
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

f(i, j) = iCj

combination nCr
0C0 = 1

1C0 = 1
1C1 = 1

2C0 = 1
2C1 = 2
2C2 = 1

3C0 = 1
3C1 = 3
3C2 = 3
3C3 = 1

4C0 = 1
4C1 = 4
4C2 = 6
4C3 = 4
4C4 = 1
"""
"""
Time Complexity: O(n^3)
Space Complexity: O()
"""

n = int(input())

for i in range(n):          # 1^2 + 2^2 + 3^2 + ... + n^2 = O(n^3)
    # time complexity: O(i^2)
    for j in range(i + 1):
        # time complexity: O(i)
        print(end=f'{combination(i, j)} ')
    print()
