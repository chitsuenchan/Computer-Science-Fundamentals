"""
    Passes 122/125 test cases
    Fail because it is Time complexity 0(n*k) which makes it inefficient for large numbers

    Can achieve a more efficient solution by:
        1. Instead of calculating the sum of the subarray in each iteration of the loop, we can maintain a running sum.
            - By updating the running sum efficiently, we avoid repeatedly summing the same elements.
            - We can slide a window of size k along the array and update the running sum accordingly.

    See the Solution file for the optimized approach
"""

def findMaxAverage(n, k):
    if k == 1:
        return max(n)

    max_avg = float('-inf')

    for i in range(len(n) - k + 1):
        # Calculate the sum of the subarray
        current_sum = sum(n[i:i+k])
        # Calculate average of the current subarray
        current_avg = current_sum / k
        # Update max_avg if the current average is greater
        max_avg = max(max_avg, current_avg)

    return max_avg


# Answer is 12.75
# print(findMaxAverage([1,12,-5,-6,50,3], 4))

lst = [0,1,1,3,3]

print(lst[:4])

print(sum(lst)/4)
end_pointer = 4

for i in range(0, len(lst) - 4 + 1):
    print(lst[i])
    slice = lst[i:end_pointer]
    print(slice)

# Answer is 2
# print(findMaxAverage([0,1,1,3,3], 4))
print(findMaxAverage([0,4,0,3,2], 1))