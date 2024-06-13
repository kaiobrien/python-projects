import string
import random
letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
password = []

for number in range(1, nr_numbers +1):
    password += random.choice(numbers)


for letter in range(1, nr_letters +1):
    password += random.choice(letters)


for symbol in range(1, nr_symbols +1):
    password += random.choice(symbols)

random.shuffle(password)
final_password = ''.join(password)

print(final_password)