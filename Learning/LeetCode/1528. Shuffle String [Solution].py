from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [''] * len(s)  # Create a list of empty strings with the same length as s

        for i, char in enumerate(s):
            result[indices[i]] = char  # Place each character of s at its corresponding index in result

        return ''.join(result)  # Join the characters in result to form the final string


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    s1 = "codeleet"
    indices1 = [4, 5, 6, 7, 0, 2, 1, 3]
    print("Example 1:")
    print("Input: s =", s1, ", indices =", indices1)
    print("Output:", solution.restoreString(s1, indices1))

    # Add more examples here if needed
