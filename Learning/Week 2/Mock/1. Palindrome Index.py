
def is_palindrome(arr):
    if arr == arr[::-1]:
        return True
    else:
        return False

def palindromeIndex(s):

    s = list(s)
    size = len(s)
    print(s)

    if is_palindrome(s):
        return -1

    for i in range(0, size // 2):
        print(i)
        if s[i] != s[size - i - 1]:
            if is_palindrome(s[:i] + s[i+1:]):
                return i
        else:
            if is_palindrome(s[:size - i - 1] + s[size-i:]):
                return size - i - 1
    return -1



palindromeIndex('bcbc')

