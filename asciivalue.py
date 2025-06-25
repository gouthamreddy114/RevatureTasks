def ascii_to_hex(input_str):
    return ' '.join(format(ord(char), ' ') for char in input_str)
print(ascii_to_hex("Aa"))