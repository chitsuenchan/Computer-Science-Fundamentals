def guessNumber(n):

    start = 1
    end = n

    while start <= end:
        mid = start + (end - start) // 2
        g = guess(mid)
        if g == 0:
            return mid
        elif g < 0:
            end = mid - 1
        else:
            start = mid + 1

    return -1  # Or handle if the number is not found within the given range

