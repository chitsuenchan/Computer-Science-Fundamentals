from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)
    result = []

    for s in strs:
        sorted_s = tuple(sorted(s))
        anagram_map[sorted_s].append(s)

    for value in anagram_map.values():
        result.append(value)

    return result


groupAnagrams(["eat","tea","tan","ate","nat","bat"])