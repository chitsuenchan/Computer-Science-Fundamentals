def superDigit(n, k):

    # Function to calculate the sum of digits of a number
    def digitSum(num):
        # Convert the number to a string
        num_str = str(num)

        # Iterate through each digit in the string representation of the number
        digits = [int(digit) for digit in num_str]

        # Calculate the sum of the digits
        digit_sum = sum(digits)

        # Call the digitSum function recursively with the calculated sum
        if digit_sum < 10:
            return digit_sum
        else:
            return digitSum(digit_sum)

    # Calculate the initial sum of digits
    initial_sum = sum(int(digit) for digit in n) * k

    # Return the result of the recursive digit sum
    return digitSum(initial_sum)

# Test the function
print(superDigit('9875', 1))
