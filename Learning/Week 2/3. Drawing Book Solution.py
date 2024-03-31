

def pageCount(n, p):

    # Calculate the number of pages to turn from the front
    # E.g. the book is n 5 so [0,1] [2,3] [4,5] and p is 5.
    # Then we will find 5/2= 2.5 which is 2 because of "//" so 2 page-turns from the front
    from_front = p // 2
    print(from_front)

    # Calculate the number of pages to turn from the back
    # "(n//2)" calculates the number of full spreads from the back to the middle of the book
    # "(p//2)" calculates the number of full spreads from the desired page, p, to the middle
    # Subtracting these gives the number of full spreads from the middle to page 'p'
    from_back = (n // 2) - (p // 2)

    # Return the minimum of the two counts
    return min(from_front, from_back)







print(pageCount(5,3))




