print('Select operator')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')

print('Enter choice: ')
num = input()

if str(num) == '1':
    print('Num1: ')
    num1 = input()
    print('Num2: ')
    num2 = input()
    print('The sum is: ' + str(int(num1)+int(num2)))
elif str(num) == '2':
    print('Num1: ')
    num1 = input()
    print('Num2: ')
    num2 = input()
    print('The Difference is: ' + str(int(num1)-int(num2)))
elif str(num) == '3':
    print('Num1: ')
    num1 = input()
    print('Num2: ')
    num2 = input()
    print('The Product is: ' + str(int(num1)*int(num2)))
elif str(num) == '4':
    print('Num1: ')
    num1 = input()
    print('Num2: ')
    num2 = input()
    if int (num2) == 0:
        print ('Invalid Input')
    else:
        print('The Quotient is: ' + str(int(num1) / int(num2)))
else:
    print('Invalid input')
