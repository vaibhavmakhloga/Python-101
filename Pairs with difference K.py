    def ncr(n, r):
    return int((fact(n) / (fact(r)
                           * fact(n - r))))


def fact(n):
    res = 1
    for i in range(2, n + 1):
        res = res * i
    return res


n = int(input())
l = list(int(i) for i in input().strip().split())
diff = int(input())
d = {}
for i in l:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i] + 1
for i in d:
    if diff == 0:
        print((str(i) + ' ' + str(i) + '\n') * ncr(d[i], 2))
    if (i + diff in d) and (diff != 0):
        print((str(i) + ' ' + str(i + diff) + '\n')
              * d[i] * d[i + diff], end='')
