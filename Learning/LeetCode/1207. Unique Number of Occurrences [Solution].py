def uniqueOccurrences(arr):
    # Count the occurrences of each number
    counter = {}
    for num in arr:
        counter[num] = counter.get(num, 0) + 1

    # Check if the counts are unique
    occurrence_set = set(counter.values())
    return len(occurrence_set) == len(counter)


print(uniqueOccurrences([1,2,2,1,1,3]))