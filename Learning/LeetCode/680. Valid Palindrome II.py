"""
    Passes 427/471

    Difficulty 7/10 - Problem is figuring out that we needed a helper function is check if the string a palindrome with that removed character

    Correct solution though just failed to return a False early in isPalindrome which makes the algorithm much faster
        Also, we use a two pointer solution. When we find matching pairs we can shrink the original word so we don't need to
        keep on checking the characters that have been already checked if they are a palindrome
"""
def validPalindrome(s):

    def isPalindrome(word):
        return word == word[::-1]

    start = 0
    end = len(s) - 1

    if isPalindrome(s):
        return True

    for i in range(len(s)):
        s_list = s[:i] + s[i + 1:]

        if isPalindrome(s_list):
            return True

    return False

# print(validPalindrome("abca"))
print(validPalindrome("deeee"))

