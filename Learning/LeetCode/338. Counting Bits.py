decimal_number = 10
binary_string = bin(decimal_number)
print(binary_string)  # Output: '0b1010'


binary_string = bin(decimal_number)[2:]
print(binary_string)  # Output: '1010'


binary_string = bin(decimal_number)[2:]  # Convert decimal to binary string without '0b' prefix
count_ones = binary_string.count('1')
print(count_ones)
