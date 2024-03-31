


def maxMin(k, arr):

    arr.sort()
    min_unfairness = float('inf')
    for i in range(len(arr) - k + 1):
        unfairness = arr[i + k - 1] - arr[i]
        if unfairness < min_unfairness:
            min_unfairness = unfairness
    return min_unfairness

maxMin(3,[38,1,10,60,50,39])