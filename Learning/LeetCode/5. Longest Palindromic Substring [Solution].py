


def longest_palindromic_substring(s: str) -> str:
    if not s:
        return ""

    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # Odd length palindromes (center at i)
        palindrome1 = expand_around_center(i, i)
        # Even length palindromes (center between i and i+1)
        palindrome2 = expand_around_center(i, i + 1)

        # Update the longest palindrome found
        if len(palindrome1) > len(longest):
            longest = palindrome1
        if len(palindrome2) > len(longest):
            longest = palindrome2

    return longest

# Example usage:
s = "babad"
print(longest_palindromic_substring(s))  # Output: "bab" or "aba"

s = "cbbd"
print(longest_palindromic_substring(s))  # Output: "bb"