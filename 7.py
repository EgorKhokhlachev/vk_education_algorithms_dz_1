arr = list(map(int,input().split(" ")))
L = 1 # длина последовательносит нулей
# Будем идти по массиву, когда находим 0 начинаем свопать их со след, когда доходим до еще нуля, увеличиваем L и свопаем уже много элементов
i = 0
while (i < len(arr)) and (arr[i] != 0):
    i = i + 1
if i == len(arr):
    print(arr)
else:
    while i < (len(arr) - 1):
        if arr[i + 1] == 0:
            L += 1
            i += 1
            continue
        else:
            tmp = arr[i - L + 1]
            arr[i - L + 1] = arr[i+1]
            arr[i + 1] = tmp
            i += 1
    print(arr)
