
"""
    Wrong solution.

    Need to update the list chars in place and return the len of it.
    E.g.

        Input: chars = ["a","a","b","b","c","c","c"]
        Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
        Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
"""

def compress(chars):

    slow = 0

    counter = 1
    for i in range(len(chars)):
        chars[slow] = chars[i]
        slow += 1

        current_char = chars[i]
        counter += 1
        print (chars[i])
        print(counter)

        if chars[i] != current_char:
            chars[slow] = counter
            counter = 1
            slow += 1

    print(chars)

compress(["a","a","b","b","c","c","c"])