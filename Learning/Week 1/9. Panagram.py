

def pangrams(s):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for letter in alphabet:
        print(letter)

        isPanagram = False

        for letterTwo in s:
            if letter.lower() == letterTwo.lower():
                isPanagram = True

        print("isPangram", isPanagram)

        if not isPanagram:
            return "not pangram"

    return "pangram"




print(pangrams("We promptly judged antique ivory buckles for the next prize"))


