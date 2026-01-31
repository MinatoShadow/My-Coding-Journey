import random

# List of uppercase letters
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

# List of lowercase letters
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

# List of digits
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# List of symbols
symbols = ["!", "@", "#", "$", "%", "&", "*", "?"]

# Display program title
print("Password Generator")

# Get password length from user
length = int(input("Enter Password Length: "))

# Get user choices for character types
char_uppercase = input("Include Uppercase Letters (y/n): ").lower()
char_lowercase = input("Include Lowercase Letters (y/n): ").lower()
char_numbers = input("Include Digits (y/n): ").lower()
char_symbols = input("Include Symbols (y/n): ").lower()

# Create an empty character pool
char_pool = []

# Check if password length is too short
if length < 4:
    print("Too Short")
    exit()

# Add uppercase letters if selected
if char_uppercase == "y" or char_uppercase == "yes":
    char_pool += uppercase

# Add lowercase letters if selected
if char_lowercase == "y" or char_lowercase == "yes":
    char_pool += lowercase

# Add numbers if selected
if char_numbers == "y" or char_numbers == "yes":
    char_pool += numbers

# Add symbols if selected
if char_symbols == "y" or char_symbols == "yes":
    char_pool += symbols

# Check if no character type was selected
if len(char_pool) == 0:
    print("You must choose atleast one character type.")
else:
    # Generate password
    password = ""

    for i in range(length):
        password += random.choice(char_pool)

    # Print the generated password
    print(f"Generated Password: {password}")
