
def bigSorting(arr):

    if len(arr) <= 1:
        return arr
    else:
        pivot = int(arr[len(arr) // 2])  # Choose the pivot element (middle element)
        arr = [int(x) for x in arr]  # Convert strings to integers for comparison
        left = [str(x) for x in arr if x < pivot]  # Elements less than pivot
        middle = [str(x) for x in arr if x == pivot]  # Elements equal to pivot
        right = [str(x) for x in arr if x > pivot]  # Elements greater than pivot
        return bigSorting(left) + middle + bigSorting(right)


print(bigSorting(['1','200','150','3']))