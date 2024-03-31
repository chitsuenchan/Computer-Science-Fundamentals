
def climbing_leaderboard(ranked, player):
    ranked = sorted(set(ranked), reverse=True)
    player_ranks = []

    print(ranked)

    j = len(ranked) - 1
    print(j)
    for score in player:
        while j >= 0 and score >= ranked[j]:
            j -= 1
        player_ranks.append(j + 2)
    return player_ranks

# Example usage:
ranked = [100, 90, 90, 80, 75, 60]
player = [50, 65, 77, 90, 102]
result = climbing_leaderboard(ranked, player)
print(result)  # Output should be [6, 5, 4, 2, 1]
