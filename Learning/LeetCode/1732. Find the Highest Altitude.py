def largestAltitude(gain):
    max_alt = 0
    current_alt = 0

    for i in range(0, len(gain)):
        current_alt += gain[i]
        max_alt = max(max_alt, current_alt)

    return max_alt

print(largestAltitude([-5,1,5,0,-7]))