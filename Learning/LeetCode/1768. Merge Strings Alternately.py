def mergeAlternately(word1, word2):
    max_position = len(word1)
    last_words = ""
    if len(word1) < len(word2):
        last_words = word2[len(word1):]

    if len(word1) > len(word2):
        last_words = word1[len(word2):]
        max_position = len(word2)

    results = []
    pointer = 0

    while pointer < max_position:
        results.append(word1[pointer])
        results.append(word2[pointer])
        pointer += 1

    if len(word1) != len(word2):
        results.extend(list(last_words))

    return "".join(results)

word1 = "abc"
word2 = "pqr"

print(mergeAlternately(word1, word2))