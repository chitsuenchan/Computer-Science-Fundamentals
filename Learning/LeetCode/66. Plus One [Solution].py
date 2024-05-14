"""
    Beats 97%
    Faster because it goes right to left iteration and stops as soon as it changes all the zeros

    Time 0(n)
    Space 0(1)
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the last digit
        for i in range(len(digits) - 1, -1, -1):
            # If the current digit is less than 9, simply increment it and return the updated list
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the current digit is 9, set it to 0 and continue to the next iteration
            else:
                digits[i] = 0

        # If all digits are 9, we need to add a new leading 1
        return [1] + digits