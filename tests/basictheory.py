BinaryTheory = {
    "Binary": ["Decimal", "Octal", "Hexadecimal"]
}


def decimalToBinary(num):
    """This function converts decimal number
    to binary and prints it"""
    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2, end='')


# decimal number
print(hex(0b1010101))
print(oct(0b101010))
print(int(0b101010))
