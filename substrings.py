def subString(s, n):
    for i in range(n):
        for len in range(i + 1, n + 1):
            print(s[i: len])


s = input()
subString(s, len(s))
