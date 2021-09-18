#A merge sort algorithm program that sorts through an array
def mergeSort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        #recursion portion of algorithm
        mergeSort(left_arr)
        mergeSort(right_arr)

        i = 0 #index of left_arr
        j = 0 #index of right_arr
        k = 0 #index of merged array
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

arr_test = [5, 4, 32, 16, 11, 9, 22, 17, 2, 3555, 232, 22]
mergeSort(arr_test)
print(arr_test)
