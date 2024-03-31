
def miniMaxSum(arr):

    lowest_to_highest_arr = sorted(arr)
    highest_to_lowest = sorted(arr,reverse=True)

    print(lowest_to_highest_arr[:4])
    print(highest_to_lowest[:4])

    min_sum = 0
    max_sum = 0

    for num in lowest_to_highest_arr[:4]:
        min_sum += num

    for num in highest_to_lowest[:4]:
        max_sum += num

    print(min_sum, max_sum)





miniMaxSum([1,3,5,7,9])