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
    y2