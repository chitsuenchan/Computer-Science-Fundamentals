
# Passes 17/18 Test cases

from collections import Counter

def isValid(s):

    occurences = {}

    for letter in s:
        if letter in occurences:
           occurences[letter] += 1
        else:
            occurences[letter] = 1

    print(occurences)
    unique_occurences = list(set(occurences.values()))

    # Count occurrences of each value
    value_counts = Counter(occurences.values())

    # Find the mode(s) - value(s) with the highest count
    max_count = max(value_counts.values())
    modes = [value for value, count in value_counts.items() if count == max_count]

    print("Mode(s):", modes)
    print("len of modes", len(modes))

    if len(modes) >= 2 and len(s) > 2:
        print("NO")
        return "NO"

    replacements_needed = 0

    for value in occurences.values():
        if value != modes[0]:
            replacements_needed += value
    print("replacements needed ", replacements_needed)


    if replacements_needed > 1:
        print("NO")
        return "NO"
    return "YES"


isValid('abcdefghhgfedecba')

