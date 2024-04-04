def strStr(s, needle):
    if len(needle) == 0:
        return 0

    for i in range(len(s)):

        sliced = s[i: i + len(needle)]
        print(sliced)

        if sliced == needle:
            return i
    return -1



print(strStr("bsadbutsad","sad"))