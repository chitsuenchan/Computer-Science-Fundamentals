
def letterCombinations(digits):
    keyboard = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    result = []
    def backtracking(i, current_string):

        # Base case
        if len(current_string) == len(digits):
            result.append(current_string)
            return
        for char in keyboard[digits[i]]:
            backtracking(i + 1, current_string + char)

    if digits:
        backtracking(0, "")

    return result

print(letterCombinations("23"))