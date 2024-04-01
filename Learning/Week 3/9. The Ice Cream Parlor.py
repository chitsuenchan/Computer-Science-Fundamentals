
def icecreamParlor(money, arr):

    flavor_map = {}

    for index, ice_cream_cost in enumerate(arr):

        cost_difference = money - ice_cream_cost

        if cost_difference in flavor_map:
            return [flavor_map[cost_difference] + 1, index + 1]

        flavor_map[ice_cream_cost] = index


# Total money
m = 9

# Costs of each flavor
arr = [1, 3, 4, 6, 7, 9]

result = icecreamParlor(m, arr)
print(result)








