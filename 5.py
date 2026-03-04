def sort012(a, arr_size):
    low = 0
    hi = arr_size - 1
    mid = 0
    while mid <= hi:
        if a[mid] == 0:
            a[low], a[mid] = a[mid], a[low]
            low += 1
            mid += 1
        elif a[mid] == 1:
            mid += 1
        else:
            a[mid], a[hi] = a[hi], a[mid]
            hi -= 1
    return a

arr = list(map(int,input().split(" ")))
arr_size = len(arr)
arr = sort012(arr, arr_size)
print(arr)

