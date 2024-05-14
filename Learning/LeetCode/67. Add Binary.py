"""
    Passes
    Beats 85%
    Difficulty 2/10 - got it straight away in 5mins
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_base10 = int(a, 2)
        b_base10 = int(b, 2)

        result_base10 = a_base10 + b_base10
        result_base2 = bin(result_base10)[2:]

        return result_base2