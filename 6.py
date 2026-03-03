arr = list(map(int,input().split(" ")))

i = 0
k = 0 # колличество четных чисел
while i < len(arr):
    if arr[i] % 2 == 0:
        tmp = arr[i]
        arr[i] = arr[k]
        arr[k] = tmp
        k += 1
    i += 1
print(*arr)