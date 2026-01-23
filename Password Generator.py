import random

# Character lists
uppercase = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

lowercase = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "@", "#", "$", "%", "&", "*", "?"]

print("Password Generator")

length = int(input("Enter Password Length: "))
char_uppercase = input("Include Uppercase Letters(y/n): ").lower()
char_lowercase = input("Include Lowercase Letters(y/n): ").lower()
char_numbers = input("Include Digits(y/n): ").lower()
char_symbols = input("Include Symbols(y/n): ").lower()

char_pool = []

if length < 4:
    print("Too Short")
    exit()
if char_uppercase == "y" or char_uppercase == "yes":
    char_pool += uppercase
if char_lowercase == "y" or char_lowercase == "yes":
    char_pool += lowercase
if char_numbers == "y" or char_numbers == "yes":
    char_pool += numbers
if char_symbols == "y" or char_symbols == "yes":
    char_pool += symbols


if len(char_pool) == 0:
    print("You must choose atleast one character type.")
else:
    password = ""

    for i in range(length):
        password += random.choice(char_pool)

    print(f"Generated Password: {password}")

