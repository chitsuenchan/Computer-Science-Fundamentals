def icecreamParlor(money, arr):

    print("Ice cream costs: {0}".format(arr))
    print("Total Money:     {0}".format(money))
    print("")

    flavor_map = {}

    for index, ice_cream_cost in enumerate(arr):

        print("index: {0}".format(index +1))
        print(" ice cream cost:  {0}".format(ice_cream_cost))

        complement = money - ice_cream_cost
        print(" Money in pocket: " + str(money))
        print(" Money - iceream: " + str(complement))


        if complement in flavor_map:
            return [flavor_map[complement] + 1, index + 1]

        flavor_map[ice_cream_cost] = index
        print(" Adding ice cream cost, {0}, to flavour map with index {1}".format(ice_cream_cost, index))
        print(" Flavor_map: {0}".format(flavor_map))
        print("")


# Total money
m = 4
m2 = 9

# Costs of each flavor
arr = [1, 4, 5, 3, 2]
arr2 = [1, 3, 4, 6, 7, 9]

result = icecreamParlor(m2, arr2)
print(result)