# continue
# for i in range(10):
#     print(i)
#     if i == 4:
#         continue

# for i in range(3):
#
#     for j in range(2):
#         print(i + j, end=' ')
#
#     print(i)
#
# print(i)
# print(j)

# i = 0
# while i < 10:
#     j = 0
#     while j < 3:
#         print(i + j, end=' ')
#         j += 1
#         i += 2
#
#     print(i)

# break
# for i in range(10):
#     print(i)
#     if i == 5:
#         break

for i in range(4):

    for j in range(2):
        if j == 1:
            break
        print(i + j, end=' ')

    print(i)

"""
output
i = 3
j = 1

0 0
1 1
2 2
3 3

"""
