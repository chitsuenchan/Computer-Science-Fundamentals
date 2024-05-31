"""
    Didn't get this at all
    Difficulty 9/10

"""
def letterCombinations(digits):
    h = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    letters_lst = []
    for digit in digits:
        letters_lst.append(h.get(digit))

    print(letters_lst)

    one = ['a', 'b', 'c']
    two = ['d', 'e', 'f']

    for _ in range(len(digits)):

        current_word = ""
        for letter in one:
            print(letter)
            current_word += letter
            for j in two:
                current_word += j
                print(" ", current_word)
                current_word = current_word[:-1]
            current_word = current_word[:-1]


letterCombinations("23")