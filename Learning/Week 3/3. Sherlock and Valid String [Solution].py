
# Passes 17/18 Test cases

from collections import Counter


def isValid(s):
    freq = Counter(s)
    print(freq)
    freq_freq = Counter(freq.values())
    print(freq_freq)
    print(len(freq_freq))

    if len(freq_freq) == 1:
        return "YES"
    elif len(freq_freq) > 2:
        return "NO"


    # If there are exactly two distinct frequencies, check if we can remove one character to make it valid
    else:
        k1, k2 = freq_freq.keys()
        v1, v2 = freq_freq.values()

        # If one of the frequencies occurs only once and is 1 greater than the other frequency,
        # or if one frequency is 1 and its count is 1, we can remove one character to make it valid
        if (v1 == 1 and (k1 - k2 == 1 or k1 == 1)) or (v2 == 1 and (k2 - k1 == 1 or k2 == 1)):
            return "YES"
        else:
            return "NO"


isValid('abcdefghhgfedecba')

