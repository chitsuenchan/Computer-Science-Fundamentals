
def is_palindrome(s):
    return s == s[::-1]

def palindromeIndex(s):
    if is_palindrome(s):
        return -1

    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            if is_palindrome(s[:i] + s[i + 1:]):
                return i
            elif is_palindrome(s[:n - 1 - i] + s[n - i:]):
                return n - 1 - i

    return -1

palindromeIndex('bcbc')
