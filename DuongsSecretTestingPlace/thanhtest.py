arr = [1,3,-3,989,463]

def selection_sort(arr):
    lenght = len(arr)
    for i in range(len(arr)):
        min = i
        for j in range(i+1, lenght):
            if arr[min] > arr[j]:
                min = j
        arr[i] , arr[min] = arr[min], arr[i]
    return arr

print(selection_sort(arr))