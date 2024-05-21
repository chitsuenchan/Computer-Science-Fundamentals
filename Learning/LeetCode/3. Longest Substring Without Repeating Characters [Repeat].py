"""
    Passes

    Good solution

    Time 0(n)
    Space: 0(n)
"""


def lengthOfLongestSubstring(s: str) -> int:

    if len(s) == 0:
        return 0

    left, right, longest_count = 0, 0, 0
    seen = set()

    while right < len(s):
        right_val = s[right]
        left_val = s[left]
        if right_val not in seen:
            seen.add(right_val)
            longest_count = max(len(seen), longest_count)
            right += 1
        else:
            while right_val in seen:
                seen.remove(left_val)
                left += 1
                left_val = s[left]
            seen.add(right_val)
            right += 1

    return longest_count



# print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("pwwkew"))