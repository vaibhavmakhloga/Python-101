def evencount(arr):
    s = set()
    d = {}
    for i in arr:
        if i not in s:
            s.add(i)
    for i in arr:
        if i in s:
            d[i] = d.get(i, 0) + 1
    for w in arr:
        if d[w] % 2 == 0:
            return w


n = int(input())
arr = list(int(i) for i in input().strip().split())
if evencount(arr):
    print(evencount(arr))
else:
    print(-1)
