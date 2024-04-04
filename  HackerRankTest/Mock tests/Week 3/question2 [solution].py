def count_pairs_with_difference_k(k, arr):
    num_count = {}

    for num in arr:
        if num not in num_count:
            num_count[num] = 1
        else:
            num_count[num] += 1

    pair_count = 0

    for num in num_count:
        if num + k in num_count:
            pair_count += num_count[num] * num_count[num + k]

    return pair_count


print(count_pairs_with_difference_k(2, [1,5,3,4,2]))