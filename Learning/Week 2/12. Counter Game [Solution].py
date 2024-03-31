def counterGame(n):
    def is_power_of_two(x):
        return (x & (x - 1)) == 0

    def highest_power_of_two(x):
        power = 0
        while x > 1:
            x //= 2
            power += 1
        return power

    player = 1
    while n > 1:
        if is_power_of_two(n):
            n -= n // 2
        else:
            n -= 2 ** highest_power_of_two(n)
        player = 1 - player

    if player == 1:
        return "Richard"
    else:
        return "Louise"

print(counterGame(1073741824))