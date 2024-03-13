#converter

#Displaying conversion options for the user
print('Choose the conversion you want to perform first:')
print('[1] - Decimal to Binary')
print('[2] - Decimal to Octal')
print('[3] - Decimal to Hexadecimal')

#Prompting the user to input their choice
print('Enter Your Choice [1/2/3]: ')
choice = input()

#Handling the user's choice and performing the selected conversion
if choice == '1':
    #Convert decimal to binary
    print('Decimal to Binary')
    print('Enter Decimal: ')
    decimal_number = input()
    binary_number = bin(int(decimal_number))
    
    print('The Binary Representation of ',decimal_number, ' is ',binary_number)

elif choice == '2':
    #Convert decimal to octal
    print('Decimal to Octal')
    print('Enter Decimal: ')
    decimal_number = input()
    octal_number = oct(int(decimal_number))

    print('The Binary Representation of ', decimal_number, ' is ', octal_number)

elif choice == '3':
    #Convert decimal to hexadecimal
    print('Enter Decimal: ')
    decimal_number = input()
    print('Decimal to Hexadecimal')
    hexa_number = hex(int(decimal_number))

    print('The Binary Representation of ', decimal_number, ' is ', hexa_number)

else:
    #Handle invalid input
    print('INVALID INPUT')
