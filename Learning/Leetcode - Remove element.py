
def removeElement(nums, val):
    results = []

    for num in nums:
        if num != val:
            results.append(num)

    print(results)
    return results


removeElement([0,1,2,2,3,0,4,2], 2)
