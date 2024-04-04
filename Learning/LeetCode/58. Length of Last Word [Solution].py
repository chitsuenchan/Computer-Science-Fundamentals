def lengthOfLastWord(s: str) -> int:
    # Trim the input string to remove leading and trailing spaces
    s = s.strip()

    # Initialize a variable to store the length of the last word
    length = 0

    # Start iterating the string from the end
    for i in range(len(s) - 1, -1, -1):
        # If a non-space character is encountered, start counting its length
        if s[i] != ' ':
            length += 1
        # If a space character is encountered after a word, return its length
        elif length > 0:
            return length
    # If no word is found, return 0
    return length


# Test cases
print(lengthOfLastWord("Hello World"))  # Output: 5
print(lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
print(lengthOfLastWord("luffy is still joyboy"))  # Output: 6