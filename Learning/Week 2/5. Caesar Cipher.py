




def caesarCipher(s, k):

    while k > 26:
        k = k - 26
    original_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabet = original_alphabet.upper()


    first_letters = original_alphabet[:k]
    last_letters = original_alphabet[k:]

    first_letters_upper = upper_alphabet[:k]
    last_letters_upper = upper_alphabet[k:]


    rotated_alphabet = last_letters + first_letters
    rotated_alphabet_upper = last_letters_upper + first_letters_upper

    print(original_alphabet)
    print(rotated_alphabet)

    print(upper_alphabet)
    print(rotated_alphabet_upper)

    mapping = {}
    mapping_upper = {}

    for letter1, letter2 in zip(original_alphabet, rotated_alphabet):
        mapping[letter1] = letter2

    for letter1, letter2 in zip(upper_alphabet, rotated_alphabet_upper):
        mapping[letter1] = letter2

    print("Letter mapping:")
    for letter1, letter2 in mapping.items():
        print(letter1, "->", letter2)

    new_word = ""
    for letter in s:
        if letter.isupper() and letter.lower() in mapping:
            lower_letter = letter.lower()

            new_word += mapping[lower_letter].upper()
        elif letter in mapping:
            new_word += mapping[letter]
        else:
            new_word += letter

    print(new_word)
    return new_word

caesarCipher('Alw',54)
# caesarCipher('Always-Look-on-the-Bright-Side-of-Life',5)