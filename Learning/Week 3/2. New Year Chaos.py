
def minimumBribes(q):

    n = len(q)
    sorted_q = sorted(q)
    print(sorted_q)
    print(q)

    for i in range(1, n + 1):

        position_old_queue = i - 1
        position_new_queue = q.index(i)

        print("number: ", i)
        print(" position in old queue: ", position_old_queue)
        print(" position in new queue: ", position_new_queue)

        difference = position_old_queue - position_new_queue
        print(" difference: ", difference)
        if difference > 2:
            print("Too chaotic")
            return

    counter = 0
    for i in range(1, n + 1):
        position_old_queue = i - 1
        position_new_queue = q.index(i)

        print("number: ", i)
        print(" old queue: ", sorted_q)
        print(" new queue: ", q)
        print(" position in old queue: ", position_old_queue)
        print(" position in new queue: ", position_new_queue)

        difference = position_old_queue - position_new_queue
        print(" difference: ", difference)

        if difference < 0:
            counter += abs(difference)

        q.remove(i)
        q.insert(i-1, i)

    print(counter)


minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])

