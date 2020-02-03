def listtoset(l):
    s1 = set()
    for i in l:
        s1.add(i)
    lol = len(lmao2) - len(s1)
    print(lol)


num = int(input())
lmao2 = [int(i) for i in input().strip().split()]
if num >= 0 and num <= 10**5:
    listtoset(lmao2)
