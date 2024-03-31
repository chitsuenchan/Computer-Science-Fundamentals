
# Passes 17/18 Test cases

from collections import Counter


def climbingLeaderboard(ranked, player):

    ranked_distinct = list(set(ranked))
    ranked_distinct.append(0)
    ranked_distinct.sort(reverse=True)
    print(ranked_distinct)
    ranks = []

    for score in player:
        print("Score is: ", score)

        rank = 1
        i = 0
        while score < ranked_distinct[i]:
            rank += 1
            i += 1
        ranks.append(rank)
        print(rank)

    return ranks



climbingLeaderboard([100, 90, 90, 80, 75,60],[50, 65, 77, 90, 102])



# 6
# 5
# 4
# 2
# 1