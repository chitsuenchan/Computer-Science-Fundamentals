def increasingTriplet(nums):
    small = float('inf')
    second_small = float('inf')

    for num in nums:
        if num <= small:
            small = num
        elif num <= second_small:
            second_small = num
        else:
            return True

    return False


# Example usage:
# nums = [1, 2, 3, 4, 5]
nums = [5,20,6,1,7]
print(increasingTriplet(nums))  # Output: True
