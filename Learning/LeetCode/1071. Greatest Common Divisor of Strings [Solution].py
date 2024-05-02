def gcdOfStrings(str1: str, str2: str) -> str:
    # Helper function to find the greatest common divisor (GCD) of two numbers
    def gcd(a, b):
        # Keep dividing the larger number by the smaller number until the remainder is zero
        while b:
            a, b = b, a % b
        return a

    # Helper function to check if a string is a divisor of another string
    def is_divisor(divisor, string):
        # Check if the given string can be formed by repeating the divisor
        for i in range(0, len(string), len(divisor)):
            # If any part of the string doesn't match the divisor, return False
            if string[i:i+len(divisor)] != divisor:
                return False
        return True

    # Find the length of the GCD of the lengths of the input strings
    gcd_len = gcd(len(str1), len(str2))

    # Extract a substring from the first string with length equal to the GCD length
    gcd_str = str1[:gcd_len]

    # Check if this substring is a divisor of both input strings
    if is_divisor(gcd_str, str1) and is_divisor(gcd_str, str2):
        # If it is, return this substring as the GCD
        return gcd_str
    else:
        # Otherwise, return an empty string, indicating there is no common divisor
        return ''
