


def birthday(s, d, m):
    results = []

    if m == 1:
        for num in s:
            if num == d:
                results.append(num)
    else:

        for i in range(0, len(s) - 1):
            cut_array = s[i:i + m]

            if sum(cut_array) == d:
                results.append(cut_array)

    return len(results)



birthday([2,2,1,3,2], 4, 2)

