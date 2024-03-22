import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*()_+}{\|:;?><'

all_chars = lower + upper + numbers + symbols
length = 8  # Corrected variable name

# Ensure the password length matches the desired length
if length < 4:
    print("Password length should be at least 4.")
else:
    password = "".join(random.sample(all_chars, length))
    print(password)
