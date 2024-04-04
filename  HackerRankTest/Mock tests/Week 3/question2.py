
def pairs(k, arr):

    pairs = {}
    count = 0

    for num in arr:
        print(num)
        left_over = abs(num - k)
        print(" left_over:",left_over)
        print(" hashmap is: ", pairs)

        if pairs.get(left_over):
            print(" FOUND left over in hashmap: ", pairs.get(left_over))

        if num not in pairs:
            pairs[num] = left_over
        print(" hashmap is: ", pairs)

    print(pairs)


pairs(2, [1,5,3,4,2])