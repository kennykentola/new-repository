

def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def binary_to_decimal(binary):
    return int(binary, 2)

def hex_addition(hex1, hex2):
    return hex(int(hex1, 16) + int(hex2, 16))[2:].upper()

def hex_subtraction(hex1, hex2):
    return hex(int(hex1, 16) - int(hex2, 16))[2:].upper()

def hex_multiplication(hex1, hex2):
    return hex(int(hex1, 16) * int(hex2, 16))[2:].upper()

def hex_division(hex1, hex2):
    if int(hex2, 16) == 0:
        return "Division by zero error"
    return hex(int(hex1, 16) // int(hex2, 16))[2:].upper()

# ADDITIONAL
def decimal_to_hexadecimal(decimal):
    return hex(decimal)[2:].upper()

def hexadecimal_to_decimal(hexadecimal):
    return int(hexadecimal, 16)

def decimal_to_octal(decimal):
    return oct(decimal)[2:]

def octal_to_decimal(octal):
    return int(octal, 8)

def hexadecimal_to_binary(hexadecimal):
    decimal_value = int(hexadecimal, 16)
    return bin(decimal_value)[2:]

def binary_to_hexadecimal(binary):
    decimal_value = int(binary, 2)
    return hex(decimal_value)[2:].upper()

def octal_to_binary(octal):
    decimal_value = int(octal, 8)
    return bin(decimal_value)[2:]

# END ADDITIONAL

def arithmetic_operation(op, num1, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Division by zero error"
    else:
        return "Invalid operator"

def logical_operation(op, num1, num2):
    if op == 'AND':
        return num1 & num2
    elif op == 'OR':
        return num1 | num2
    elif op == 'XOR':
        return num1 ^ num2
    elif op == 'NOT':
        return ~num1
    elif op == 'ShiftLeft':
        return num1 << num2
    elif op == 'ShiftRight':
        return num1 >> num2
    elif op == 'RotateLeft':
        return (num1 << num2) | (num1 >> (32 - num2))
    elif op == 'RotateRight':
        return (num1 >> num2) | (num1 << (32 - num2))
    else:
        return "Invalid operation"

while True:
    print("Choose an option:")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")
    print("3. Hexadecimal Addition")
    print("4. Hexadecimal Subtraction")
    print("5. Hexadecimal Multiplication")
    print("6. Hexadecimal Division")
    print("7. Arithmetic Operation (+, -, *, /)")
    print("8. Logical Operation (AND, OR, XOR, NOT, ShiftLeft, ShiftRight, RotateLeft, RotateRight)")
    # ADDITIONAL BEGIN
    print("9. Decimal to Hexadecimal")
    print("10. Hexadecimal to Decimal")
    print("11. Decimal to Octal")
    print("12. Octal to Decimal")
    print("13. Hexadecimal to Binary")
    print("14. Binary to Hexadecimal")
    print("15. Octal to Binary")
    print("16. Binary to Octal")
    print("17. Hexadecimal to Octal")
    print("18. Octal to Hexadecimal")
    # END ADDITIONAL
    print("19. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19): ")

    if choice == '19':
        print("Exiting the calculator.")
        break

    try:
        if choice in ('1', '2', '3', '4', '5', '6', '7', '8'):
            if choice == '1':
                decimal_number = int(input("Enter the decimal number: "))
                binary_result = decimal_to_binary(decimal_number)
                print(f"Binary: {binary_result}")
            elif choice == '2':
                binary_number = input("Enter the binary number: ")
                decimal_result = binary_to_decimal(binary_number)
                print(f"Decimal: {decimal_result}")
            elif choice == '3':
                hex_num1 = input("Enter the first hexadecimal number: ")
                hex_num2 = input("Enter the second hexadecimal number: ")
                result = hex_addition(hex_num1, hex_num2)
                print(f"Result: {result}")
            elif choice == '4':
                hex_num1 = input("Enter the first hexadecimal number: ")
                hex_num2 = input("Enter the second hexadecimal number: ")
                result = hex_subtraction(hex_num1, hex_num2)
                print(f"Result: {result}")
            elif choice == '5':
                hex_num1 = input("Enter the first hexadecimal number: ")
                hex_num2 = input("Enter the second hexadecimal number: ")
                result = hex_multiplication(hex_num1, hex_num2)
                print(f"Result: {result}")
            elif choice == '6':
                hex_num1 = input("Enter the first hexadecimal number: ")
                hex_num2 = input("Enter the second hexadecimal number: ")
                result = hex_division(hex_num1, hex_num2)
                print(f"Result: {result}")
            elif choice == '7':
                operator = input("Enter the operator (+, -, *, /): ")
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = arithmetic_operation(operator, num1, num2)
                print(f"Result: {result}")
            elif choice == '8':
                operator = input("Enter the logical operation (AND, OR, XOR, NOT, ShiftLeft, ShiftRight, RotateLeft, RotateRight): ")
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                result = logical_operation(operator, num1, num2)
                print(f"Result: {result}")
        # ADDITIONAL BEGIN
        elif choice in ('9', '10', '11', '12', '13', '14', '15', '16', '17', '18'):
            number = input("Enter the number: ")
            if choice == '9':
                result = decimal_to_hexadecimal(int(number))
                print(f"Hexadecimal: {result}")
            elif choice == '10':
                result = hexadecimal_to_decimal(number)
                print(f"Decimal: {result}")
            elif choice == '11':
                result = decimal_to_octal(int(number))
                print(f"Octal: {result}")
            elif choice == '12':
                result = octal_to_decimal(number)
                print(f"Decimal: {result}")
            elif choice == '13':
                result = hexadecimal_to_binary(number)
                print(f"Binary: {result}")
            elif choice == '14':
                result = binary_to_hexadecimal(number)
                print(f"Hexadecimal: {result}")
            elif choice == '15':
                result = octal_to_binary(number)
                print(f"Binary: {result}")
            elif choice == '16':
                decimal_value = binary_to_decimal(number)
                result = decimal_to_octal(decimal_value)
                print(f"Octal: {result}")
            elif choice == '17':
                result = hexadecimal_to_octal(number)
                print(f"Octal: {result}")
            elif choice == '18':
                result = octal_to_hexadecimal(number)
                print(f"Hexadecimal: {result}")
        # END ADDITIONAL
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19).")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        print("Division by zero error.")
