
def findMaxAverage(nums, k):
    # Calculate the sum of the first window of size k
    current_sum = sum(nums[:k])
    max_avg = current_sum / k

    # Slide the window along the array and update max_avg if necessary
    for i in range(1, len(nums) - k + 1):
        # Subtract the element leaving the window and add the new element entering the window
        current_sum = current_sum - nums[i - 1] + nums[i + k - 1]
        max_avg = max(max_avg, current_sum / k)

    return max_avg


# Answer is 12.75
# print(findMaxAverage([1,12,-5,-6,50,3], 4))

# Answer is 2
# print(findMaxAverage([0,1,1,3,3], 4))
print(findMaxAverage([0,4,0,3,2], 1))