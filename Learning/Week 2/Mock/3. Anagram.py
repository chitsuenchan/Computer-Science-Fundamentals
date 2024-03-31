

def anagram(s):
    s = list(s)

    if len(s) == 1:
        return -1
    elif len(s) == 2:
        return 1
    elif len(s) % 2 != 0:
        return -1

    middle_index = len(s) // 2
    s1 = sorted(s[:middle_index])
    s2 = sorted(s[middle_index:])

    count_changes = 0
    for char1, char2 in zip(s1, s2):
        if char1 != char2:
            count_changes += 1

    return count_changes

anagram("csgokgibmftzeozyadcofpouaerckbbpwhdg")



