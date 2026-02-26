str = input()
arr = list(map(int,str.split(', ')))
k = int(input())
# k - чило элиментов, которые будут сдвигаться
# с - индекс массива с которого начинается разворот массива

def reverse_array(arr,n,k):
    temp = 0
    for i in range((k - n) // 2):
        tmp = arr[n + i]
        arr[n + i] = arr[k - 1 - i]
        arr[k - 1 - i] = tmp
    return arr

arr = reverse_array(arr,0,len(arr))
arr = reverse_array(arr, 0, k)
arr = reverse_array(arr,k, len(arr))

print(arr)
