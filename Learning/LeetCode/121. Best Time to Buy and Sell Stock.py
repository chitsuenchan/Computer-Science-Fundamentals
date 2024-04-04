def maxProfit(prices):

    pointer = 0
    max_profit = 0

    for i in range(1, len(prices)):
        if prices[i] < prices[pointer]:
            pointer = i
        else:

            profit = prices[i] - prices[pointer]
            max_profit = max(max_profit, profit)

    return max_profit



print(maxProfit([7,6,4,3,1]))