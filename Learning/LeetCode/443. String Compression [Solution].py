def compress(chars):
    if len(chars) <= 1:
        return len(chars)

    write_index = 0  # Index to write the compressed characters
    count = 1  # Counter for consecutive characters
    for i in range(1, len(chars)):
        if chars[i] == chars[i - 1]:
            count += 1
        else:
            chars[write_index] = chars[i - 1]
            write_index += 1
            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1
            count = 1

    # Write the last character and its count
    chars[write_index] = chars[-1]
    write_index += 1
    if count > 1:
        for digit in str(count):
            chars[write_index] = digit
            write_index += 1

    return write_index


# Example usage:
chars = ["a", "a", "b", "b", "c", "c", "c"]
print(compress(chars))  # Output: 6
print(chars[:6])  # Output: ["a", "2", "b", "2", "c", "3"]
