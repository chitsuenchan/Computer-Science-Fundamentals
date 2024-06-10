def firstUniqChar(s):

    mapping = {}

    for letter in s:
        if letter in mapping:
            mapping[letter] += 1
        else:
            mapping[letter] = 1

    for index in range(len(s)):
        if mapping[s[index]] == 1:
            return index


print(firstUniqChar("loveleetcode"))