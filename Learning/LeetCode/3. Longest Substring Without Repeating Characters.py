"""
    Passes
    Beats 72%

    Good solution

    Time 0(n)
    Space: 0(n)
"""


def lengthOfLongestSubstring(s: str) -> int:

    if len(s) == 0:
        return 0

    highest = 0
    start = 0
    end = 0
    substring = set()
    counter = 0

    while start < len(s):
        if s[start] not in substring:
            substring.add(s[start])
            counter += 1
            start += 1
        else:
            highest = max(counter, highest)

            while s[end] != s[start]:
                substring.remove(s[end])
                counter -= 1
                end += 1

            end += 1
            start += 1

    highest = max(counter, highest)

    return highest

print(lengthOfLongestSubstring("abcabcbb"))