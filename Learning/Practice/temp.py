def convert(s):
    mapping = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }

    pointer = 0
    results = 0

    while pointer < len(s):
        print(pointer)
        print(s[pointer])

        if pointer != len(s) - 1:
            two_letters = s[pointer] + s[pointer + 1]
            print(two_letters)

            if two_letters in mapping:
                results += mapping[two_letters]
                pointer += 2
            else:
                print("adding ", mapping[s[pointer]])
                results += mapping[s[pointer]]
                pointer += 1
        else:
            results += mapping[s[pointer]]
            pointer += 1
    return results



s = "MCMXCIV"

convert(s)
