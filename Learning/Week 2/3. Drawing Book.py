

def pageCount(n, p):

    if n % 2 == 0 and n > 2 and p == n -1 or p == n -2:
        return 1

    pages = [x for x in range(n + 1)]
    pages_backwards = sorted(pages, reverse=True)

    turningMethods = [pages,pages_backwards]

    results = []

    for pages in turningMethods:
        counter = 0
        for i in range(0, n + 1):
            if i % 2 == 0:
                print(pages[i:i + 2])

                for number in pages[i:i + 2]:
                    if number == p:
                        print("FOUND THE PAGE")
                        results.append(counter)
                counter += 1

    return min(results)





print(pageCount(2,1))




