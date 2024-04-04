

def lengthOfLastWord(s):
    if s == "":
        return 0

    s = s.strip()
    lst = s.split()
    last = lst[-1]
    return len(last)


print(lengthOfLastWord("   fly me   to   the moon  "))
print(lengthOfLastWord("Hello World"))