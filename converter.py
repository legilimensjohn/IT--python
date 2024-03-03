#converter

print('Choose the conversion you want to perform first:')
print('[1] - Decimal to Binary')
print('[2] - Decimal to Octal')
print('[3] - Decimal to Hexadecimal')

print('Enter Your Choice [1/2/3]: ')
choice = input()

if choice == '1':
    print('Decimal to Binary')
    print('Enter Decimal: ')
    decimal_number = input()
    binary_number = bin(int(decimal_number))
    print('The Binary Representation of ',decimal_number, ' is ',binary_number)
elif choice == '2':
    print('Decimal to Octal')
    print('Enter Decimal: ')
    decimal_number = input()
    octal_number = oct(int(decimal_number))
    print('The Binary Representation of ', decimal_number, ' is ', octal_number)
elif choice == '3':
    print('Enter Decimal: ')
    decimal_number = input()
    print('Decimal to Hexadecimal')
    hexa_number = hex(int(decimal_number))
    print('The Binary Representation of ', decimal_number, ' is ', hexa_number)
else:
    print('INVALID INPUT')
