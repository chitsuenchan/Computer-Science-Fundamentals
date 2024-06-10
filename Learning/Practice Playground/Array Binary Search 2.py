
def binary_search_iterative(nums, target):

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


def binary_search_recursively_improved(nums, target, start=0, end=None):

    if end is None:
        end = len(nums) - 1

    if start > end:
        return False

    mid = (start + end) // 2

    if nums[mid] == target:
        return True
    elif nums[mid] < target:
        return binary_search_recursively_improved(nums, target, mid + 1, end)
    else:
        return binary_search_recursively_improved(nums, target, start, mid - 1)





n = [20, 50, 30, 14, 29, 99, 2, 100]



# Sort the array first
n.sort()

print(binary_search_iterative(n, 30))
print(binary_search_recursively_improved(n, 2))
