def strStr(s, needle):
    if len(needle) == 0:
        return 0

    letters_redundant_to_check = len(needle) - 1

    for i in range(len(s) - letters_redundant_to_check):

        for j in range(len(needle)):
            if s[i + j] != needle[j]:
                break
            if j == len(needle) - 1:
                return i
    return -1


print(strStr("bsadbutsad", "sad"))
