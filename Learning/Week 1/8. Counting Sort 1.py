

def countingSort(arr):
    # Write your code here

    freq_arr = [0 for _ in range(100)]
    print(freq_arr)

    for i in range(0, len(arr)):
        arr_number = arr[i]
        freq_arr[arr_number] += 1

    return freq_arr


countingSort([1,1,3,2,1])

