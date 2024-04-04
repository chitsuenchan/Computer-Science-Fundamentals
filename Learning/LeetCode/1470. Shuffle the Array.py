
def shuffle(nums):
    first_arr = nums[: len(nums )//2]
    last_arr = nums[len(nums )// 2:]
    results = []

    for i in range(len(first_arr)):
        results.append(first_arr[i])
        results.append(last_arr[i])

    return results


shuffle([1,1,2,2])