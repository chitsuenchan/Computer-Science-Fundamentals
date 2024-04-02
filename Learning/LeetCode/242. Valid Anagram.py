
# https://leetcode.com/problems/valid-anagram/description/?envType=study-plan-v2&envId=top-interview-150

# Hashmap, String, Sorting

def isAnagram(s, t):

    sort_s = sorted(s)
    sort_t = sorted(t)

    if len(s) != len(t):
        return False

    for i in range(len(sort_s)):
        if sort_s[i] != sort_t[i]:
            return False
    return True

isAnagram("anagram", "nagaram")