def dynamicArray(n, queries):
    seq_list = [[] for _ in range(n)]
    last_answer = 0
    result = []

    for query in queries:
        q_type, x, y = query
        index = (x ^ last_answer) % n

        if q_type == 1:
            seq_list[index].append(y)
        elif q_type == 2:
            size = len(seq_list[index])
            last_answer = seq_list[index][y % size]
            result.append(last_answer)

    return result

dynamicArray(2, [[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]])
