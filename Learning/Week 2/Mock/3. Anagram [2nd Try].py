

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

    count = 0
    for char in s1:
        if char in s2:
            s2.remove(char)
        else:
            count += 1

    return count



anagram("csgokgibmftzeozyadcofpouaerckbbpwhdg")



