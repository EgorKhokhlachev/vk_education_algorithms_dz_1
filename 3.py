arr_1 = list(map(int,input().split(" ")))
arr_2 = list(map(int,input().split(" ")))
k = len(arr_2)
# k - чило элиментов, которые будут сдвигаться
# с - индекс массива с которого начинается разворот массива

def reverse_array(arr,n,k):
    temp = 0
    for i in range((k - n) // 2):
        tmp = arr[n + i]
        arr[n + i] = arr[k - 1 - i]
        arr[k - 1 - i] = tmp
    return arr

arr_1 = reverse_array(arr_1,0,len(arr_1))
arr_1 = reverse_array(arr_1, 0, k)
arr_1 = reverse_array(arr_1,k, len(arr_1))

#print(arr_1)

i = 0
j = 0

while (i < (len(arr_1)-len(arr_2))) or (j < len(arr_2)):
    if (i == len(arr_1) - len(arr_2)):
        while j < len(arr_2):
            arr_1[i + j] = arr_2[j]
            j += 1
        break
    if (j == len(arr_2)):
        while i < (len(arr_1)-len(arr_2)):
            arr_1[i - 1 + j] = arr_1[len(arr_2) - 1 + i]
            i += 1
        break
    if arr_1[len(arr_2) + i] <= arr_2[j]:
        arr_1[i + j] = arr_1[len(arr_2)+ i]
        i += 1
    else:
        arr_1[i + j] = arr_2[j]
        j += 1

    print(arr_1,"i - ",i,"j -",j)

print(arr_1)