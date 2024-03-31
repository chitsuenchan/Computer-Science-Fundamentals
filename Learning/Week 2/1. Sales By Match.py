def sockMerchant(n, ar):

    unique_numbers = list(set(ar))

    total_number_of_pairs = 0

    for unique_number in unique_numbers:

        count = 0
        for number in ar:
            if number == unique_number:
                count += 1

        if count % 2 == 0:
            unique_number_pairs = count / 2
        else:
            unique_number_pairs = count - 1 / 2

        total_number_of_pairs += unique_number_pairs

    return total_number_of_pairs



sockMerchant(7, [1,2,1,2,1,3,2])