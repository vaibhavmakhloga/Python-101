n = int(input())
arr = [int(i) for i in input().strip().split()]

for i in range(n):
    k = 0
    for j in range(i + 1, n):
        if arr[i] < arr[j]:
            break
        k += 1
    if k == n - (i + 1):
        print(arr[i], end=' ')
