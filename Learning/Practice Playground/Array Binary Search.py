
def binary_search_iterative(nums, target):

    # Sort the nums array
    nums.sort()
    # Initialise left and right pointers
    left, right = 0, len(nums) - 1

    # Create while loop to iterate until left is greater than or equal right
    while left <= right:
        # Inside while loop calculate the mid index and find its value
        mid = (left + right) // 2

        # If target value is mid value then break and return
        if nums[mid] == target:
            return True
        # If target value is greater than mid value we need to shift left pointer to mid + 1
        elif nums[mid] < target:
            left = mid + 1
        # If target value is less than mid value we need to shift right pointer mid - 1
        else:
            right = mid - 1

    return False

"""
    First attempt below without any outside help.
    This could be improved because slicing the array always creates a new array.
    
    See the improved algorithm after
"""

def binary_search_recursively(nums, target):

    # Base case 1 - Reached end
    if not nums:
        return False

    # Calculate the middle index
    mid = len(nums) // 2

    # Base case 2 - Found the target value
    if nums[mid] == target:
        return True

    # Recursive step
    if nums[mid] < target:
        found = binary_search_recursively(nums[mid + 1:], target)
    else:
        found = binary_search_recursively(nums[:mid], target)

    return found

"""
    This is the improved binary search algorithm with recursion.
    
    In this implementation we are adding two new paramters to the function which is start and end
        start defaults to 0
        end defaults to None
        
        This is so that we don't have to pass in the start and end values when we first call the binary
        search. the end is calculated for us in the first call
        
    
    We can also simply return the binary_search_recursively_improved and not return a found.
        This is because if we don't hit the base case at the start we go into the recursive steps
        which will eventually hit the base case of either True or False
"""
def binary_search_recursively_improved(nums, target, start=0, end=None):

    # Calculate the end pointer if no end was passed in
    #   This saves extra parameters from being passed in
    if end is None:
        end = len(nums) - 1

    # Base case 2 - range is empty
    if start > end:
        return False

    mid = (start + end) // 2

    # Base case 2 - found the target value
    if nums[mid] == target:
        return True

    elif nums[mid] < target:
        return binary_search_recursively_improved(nums, target, mid + 1, end)
    else:
        return binary_search_recursively_improved(nums, target, start, mid - 1)


n = [20, 50, 30, 14, 29, 99, 2, 100]

print(binary_search_iterative(n, 30))

# Sort the array first
n.sort()
print(binary_search_recursively(n, 180))
print(binary_search_recursively_improved(n, 180))
