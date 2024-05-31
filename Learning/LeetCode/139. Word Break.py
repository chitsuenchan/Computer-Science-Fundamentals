class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_end_of_word

    def starts_with(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True


def wordBreak(s, wordDict):

    trie = Trie()
    for word in wordDict:
        trie.insert(word)

    current_word = ""
    result = []
    result_word_count = 0
    for i in range(len(s)):
        print("current letter is", s[i])
        current_word += s[i]

        isInTrie = trie.starts_with(current_word)
        print(" in trie:", isInTrie)

        if current_word != "" and not isInTrie:
            result.append(current_word[:-1])
            print("  word is", current_word)
            print("  word count is", len(current_word))
            result_word_count += len(current_word) -1
            current_word = ""
            print("  Added word to list", result)
            print("  Added to word count", result_word_count)
            print("  Resetted current_word to empty")

            current_word += s[i]
            isInTrie = trie.starts_with(current_word)
            print("  Added current char to current_word", current_word)
            print(" in trie:", isInTrie)

            if not isInTrie:
                current_word = ""

    if current_word != "" and trie.starts_with(current_word):
        result.append(current_word)
        result_word_count += len(current_word)

    print(result)
    print(result_word_count)

    if result_word_count == len(s):
        return True
    return False




# wordBreak("applepenapple", ["apple", "pen"])
# print(wordBreak("leetcode", ["leet", "code"]))
print(wordBreak("abcd", ["a","abc","b","cd"]))

