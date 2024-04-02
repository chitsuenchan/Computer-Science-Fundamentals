
def isIsomorphic(s, t):

    mapping = {}

    for i in range(len(s)):

        if s[i] not in mapping and t[i] in mapping.values():
            return False

        if s[i] not in mapping:
            mapping[s[i]] = t[i]

        elif mapping.get(s[i]) != t[i]:
            return False

    return True



# print(isIsomorphic("egg", "add"))
# print(isIsomorphic("foo", "bar"))
# print(isIsomorphic("badc", "baba"))
print(isIsomorphic("paper", "title"))