import math

def counterGame(n):
    def is_power_of_two_func(n):
        # Check if n is a positive integer
        if not isinstance(n, int) or n <= 0:
            return False

        # Check if n has only one bit set to 1 in its binary representation
        return n & (n - 1) == 0

    def play_game(n):

        is_power_of_two = is_power_of_two_func(n)

        if is_power_of_two:
            n = int(n / 2)
            return n
        else:
            next_lowest_power = int(math.log(n,2))
            next_lower_power_of_two = 2 ** next_lowest_power
            n = n - next_lower_power_of_two
            return n

    is_louise_winner = False
    while n != 1:
        n = play_game(n)
        is_louise_winner = not is_louise_winner

    if is_louise_winner:
        return "Louise"
    return "Richard"


print(counterGame(1073741824))