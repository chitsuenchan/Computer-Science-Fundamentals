"""
    Passes
    Beats 99% of submissions

    This is the optimal solution
"""

def firstPalindrome(words):

    def isPalindrome(word):
        return word[::-1] == word

    for word in words:
        if isPalindrome(word):
            return word

    return ""

print(firstPalindrome(["abc","car","ada","racecar","cool"]))