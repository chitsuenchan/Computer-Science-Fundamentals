"""
    Passes all tests

    Same as optimized solution in terms of space and time complexity.
    However, optimized solutions utilizes the set with hashmap to tackle this problem and makes the code
    very concise
"""

def uniqueOccurrences(arr):
    h = {}

    for num in arr:
        if num in h:
            h[num] += 1
        else:
            h[num] = 1

    freq_counter = {}

    for value in h.values():
        if value in freq_counter:
            freq_counter[value] += 1
        else:
            freq_counter[value] = 1

    for value in freq_counter.values():
        if value > 1:
            return False

    return True

    print(h)
    print(freq_counter)

print(uniqueOccurrences([1,2,2,1,1,3]))