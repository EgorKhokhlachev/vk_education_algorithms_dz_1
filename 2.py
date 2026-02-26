arr_1 = list(map(int,input().split(" ")))
arr_2 = list(map(int,input().split(" ")))

def merge(arr_1,arr_2):
    i = 0
    j = 0
    merge_arr = []
    while (i < len(arr_1) or (j < len(arr_2))):
        if (i == len(arr_1)):
            while j < len(arr_2):
                merge_arr.append(arr_2[j])
                j = j+1
            return merge_arr
        if (j == len(arr_1)):
            while i < len(arr_1):
                merge_arr.append(arr_1[i])
                i = i + 1
            return merge_arr
            
        if arr_1[i] <= arr_2[j]:
            merge_arr.append(arr_1[i])
            i = i+1
        else:
            merge_arr.append(arr_2[j])
            j = j + 1
    return merge_arr
print(merge(arr_1,arr_2))
