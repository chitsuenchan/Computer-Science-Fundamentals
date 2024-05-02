def mergeAlternately(word1, word2):
    result = ''
    i = j = 0
    while i < len(word1) and j < len(word2):
        result += word1[i] + word2[j]
        i += 1
        j += 1

    result += word1[i:]
    result += word2[j:]

    return result

word1 = "abc"
word2 = "pqr"

print(mergeAlternately(word1, word2))