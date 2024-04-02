# https://leetcode.com/problems/word-pattern/description/?envType=study-plan-v2&envId=top-interview-150

# HashTab, String

def wordPattern(pattern, s):

    mapping = {}

    word_list = s.split()

    if len(s) == 1:
        return True
    if len(pattern) != len(word_list):
        return False

    for i in range(len(pattern)):

        if pattern[i] not in mapping and word_list[i] in mapping.values():
            return False

        if pattern[i] not in mapping:
            mapping[pattern[i]] = word_list[i]

        elif mapping.get(pattern[i]) != word_list[i]:
            return False
    return True




print(wordPattern("abba", "dog cat cat dog"))
print(wordPattern("aaaa", "dog cat cat dog"))
print(wordPattern("abba", "dog dog dog dog"))