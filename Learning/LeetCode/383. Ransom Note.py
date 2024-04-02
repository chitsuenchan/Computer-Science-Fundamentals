
def canConstruct(note, magazine):

    hashmap_note = {}
    hashmap_mag = {}

    for letter in note:
        if letter not in hashmap_note:
            hashmap_note[letter] = 1
        else:
            hashmap_note[letter] += 1

    for letter in magazine:
        if letter not in hashmap_mag:
            hashmap_mag[letter] = 1
        else:
            hashmap_mag[letter] += 1

    for key in hashmap_note:

        if key not in hashmap_mag:
            return False

        if hashmap_note[key] > hashmap_mag[key]:
            return False
    return True

print(canConstruct("aa", "ab"))