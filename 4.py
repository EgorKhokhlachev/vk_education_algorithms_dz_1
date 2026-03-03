arr = list(map(int,input().split(" ")))
i = 0
j = len(arr) - 1
while i < j:
    if arr[i] != 1:
        i += 1
    if arr[j] != 0:
        j -= 1
    if (arr[i] == 1) and (arr[j] == 0):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp

print(arr)
