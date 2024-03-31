
def removeDuplicates(lst):
    print("hello")

    lst.sort()
    print(lst)

    results = []
    for num in lst:
        if num not in results:
            results.append(num)

    return len(results)

removeDuplicates([1,1,1,2,2,3])
