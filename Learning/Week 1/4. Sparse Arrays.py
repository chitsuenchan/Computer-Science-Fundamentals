



def matchingStrings(strings, queries):

    list_of_sums = []

    for query in queries:

        query_sum = 0

        for string in strings:
            if string == query:
                query_sum += 1

        list_of_sums.append(query_sum)

    print(list_of_sums)




matchingStrings(['ab','ab','tt'],['ab','abc','bc'])