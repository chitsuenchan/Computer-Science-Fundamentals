def reverseVowels(s) -> str:
    v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    if len(s) == 1:
        return s

    start_p = 0
    end_p = len(s) - 1
    s = list(s)

    while start_p < end_p:
        if s[start_p] in v and s[end_p] in v:
            s[start_p], s[end_p] = s[end_p], s[start_p]
            start_p += 1
            end_p -= 1

        if s[start_p] not in v:
            start_p += 1

        if s[end_p] not in v:
            end_p -= 1
    return "".join(s)

s = "leetcode"

print(reverseVowels(s))