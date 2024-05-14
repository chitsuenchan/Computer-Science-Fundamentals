"""
    Passed
    Beats 77%
    Difficulty 5/10
         Important thing to note is whenever dealing with anagrams it's best to sort them
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        h = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in h:
                h.get(sorted_word).append(word)
            else:
                h[sorted_word] = [word]
        result = []
        for list in h.values():
            result.append(list)
        return result