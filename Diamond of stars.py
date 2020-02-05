row = int(input())
d = ('*' * (n if n <= row else 2 * row - n) for n in range(1, 2 * row, 2))
for i in d:

    print('{:^{w}}'.format(i, w=row))
