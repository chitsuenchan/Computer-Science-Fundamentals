
def dynamicArray(n, queries):
    # print("n:", n)
    empty_arrays = [[] for _ in range(n)]
    last_answer = 0
    results = []
    print(empty_arrays)

    for query in queries:
        print("query is: ", query)

        query_type, x, y = query

        if query_type == 1:
            idx = ((x ^ last_answer) % n)
            # print("idx is:", idx)
            empty_arrays[idx].append(y)
            # print("Appending " + str(y) + " to arr[" +str(idx)+"]")
            print(empty_arrays[idx])

        elif query_type == 2:
            idx = ((x ^ last_answer) % n)
            last_answer = empty_arrays[idx][y % len(empty_arrays[idx])]
            print(last_answer)
            results.append(last_answer)
    return results

dynamicArray(2, [[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]])
