import pyfiglet as pyfiglet
from os import system as system
#from textblob import TextBlob

main = py.figletFormat ("       Cryption")
print (main, "                 [*]encryp & decryp text data's[*]")

def format():
    main = py.figletFormat ("       Cryption")
print (main, "                 [*]encryp & decryp text data's[*]")

def encrypt():
    print()
    data_1 = input("Kindly enter text: ")
    encryptHash = input("Kindly enter hash: ")
    data = data_1.replace("","=")

    x1 = data.encode()

    replace1 = len(data)-1//len(encryptHash) + 1
    y2 =(encryptHash * replace1) [:len(data)].encode()

    data = bytes ([i1 i2 for (i1, i2) in zip (x1, y2)])
    print (f"The Encrypt text is: {data.decode()}")

    def encrypt():
        data = input('Kindly enter text: ')
        decrypHash = input('Kindly enter hash: ')

        z3 = data.encode()

        replace2 = len(data)-1//len(decrypHash) + 1
        w4 = (decrypHash*replace2)[:len(data)].encode()

        data_1 = bytes ([i1 i2 for (i1, i2) in zip (z3, w4)])
        decryp_data = data_1.decode()
        data_string = string(decryp_data)
        data = data_string.replaces("-", "")
        print(f"The Decrypt text is: {data}")