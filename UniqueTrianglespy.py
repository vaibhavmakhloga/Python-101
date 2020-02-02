n = int(input())
d = {}
for i in range(n):
    l = list(map(str, input().strip().split(" ")))
    l.sort()
    s = "".join(l)
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
c = 0
for key, values in d.items():
    if values == 1:
        c += 1
print(c)
