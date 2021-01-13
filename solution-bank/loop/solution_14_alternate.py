# print('1/' + str(3))
# print(f'hello world 1/{12 * 23}')

n = int(input())

for i in range(1, n + 1):
    if i == 1:
        print(end='1 + ')
    else:
        print(end=f'1/{i}' if i == n else f'1/{i} + ')
