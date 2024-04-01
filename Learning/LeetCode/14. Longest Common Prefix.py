


def longestCommonPrefix(strs):

    if not strs:
        return ""

    shortest_word = min(strs, key=len)

    for i, char in enumerate(shortest_word):
        print(i, char)

        for other_word in strs:
            if other_word[i] != char:
                return shortest_word[:i]

    return shortest_word


longestCommonPrefix(["flower","flow","flight"])