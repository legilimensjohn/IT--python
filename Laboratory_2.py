# Basic Calculator

print("Calculator")
print("Select operator")
print("[1] Sum")
print("[2] Difference")
print("[3] Product")
print("[4] Quotient")

print("Please provide your selection: ")
num = input()

if str(num) == "1":
    print("Num1: ")
    num1 = input()
    print("Num2: ")
    num2 = input()
    print("The sum is: " + str(int(num1) + int(num2)))
elif str(num) == "2":
    print("Num1: ")
    num1 = input()
    print("Num2: ")
    num2 = input()
    print("The Difference is: " + str(int(num1) - int(num2)))
elif str(num) == "3":
    print("Num1: ")
    num1 = input()
    print("Num2: ")
    num2 = input()
    print("The Product is: " + str(int(num1) * int(num2)))
elif str(num) == "4":
    print("Num1: ")
    num1 = input()
    print("Num2: ")
    num2 = input()
    if int(num2) == 0:
        print("Invalid Input")
    else:
        print("The Quotient is: " + str(int(num1) / int(num2)))
else:
    print("Invalid input")
