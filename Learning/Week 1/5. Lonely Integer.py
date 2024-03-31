def lonelyinteger(numbers):

    for number in numbers:

        counter = 0

        for numberTwo in numbers:
            if number == numberTwo:
                counter += 1

        if counter == 1:
            return number



print(lonelyinteger([1,1,1,2,4,4,2,2,10]))