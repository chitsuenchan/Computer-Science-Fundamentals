

"""
    Passes 120/124 Test cases but not correct solution

    It doesn't pass the test case:

    str1 = "AAAAAAAAA"
    str 2 = "AAACCC"

"""


def gcd(a, b):
    """
    Calculate the greatest common divisor (GCD) of two integers.

    Args:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return a


def largest_common_factor(num1, num2):
    """
    Calculate the largest common factor of two integers.

    Args:
    num1 (int): The first integer.
    num2 (int): The second integer.

    Returns:
    int: The largest common factor of num1 and num2.
    """
    return gcd(num1, num2)


# Example usage:
num1 = 36
num2 = 24
print("The largest common factor of", num1, "and", num2, "is:", largest_common_factor(num1, num2))


def gcdOfStrings(s1, s2):

    lcf = largest_common_factor(len(s1), len(s2))

    ds = s2[:lcf]
    ds_count = 0
    pointer = 0

    while pointer < len(s1):

        if s1[pointer] != ds[ds_count]:
            return ""

        pointer += 1
        ds_count += 1

        if ds_count == len(ds):
            ds_count = 0

    return ds



print(gcdOfStrings("ABABAB", "ABAB"))