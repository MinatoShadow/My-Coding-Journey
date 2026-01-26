import random
import time

# ---------- USER SETUP ---------- #
user_name = input("Enter Username: ")

# Keep asking until username is valid
while len(user_name) > 20:
    print("Username can't be more than 20 characters.")
    user_name = input("Enter Username: ")

user_pin = input("Make a Pincode: ")

# ---------- BANK BALANCE SETUP ---------- #
bank_balance = 0

# Assign random balance based on username length
if len(user_name) <= 6:
    bank_balance = random.randint(1, 25000)
elif len(user_name) <= 12:
    bank_balance = random.randint(1, 50000)
else:  # length 13–20
    bank_balance = random.randint(1, 100000)

print(f"\nYour Bank Balance Is: {bank_balance}")

# ---------- MAIN LOOP ---------- #
while True:
    # Show menu every time
    print(
        """
1. Deposit Money
2. Withdraw Money
3. Exit
"""
    )

    user_command = input("Enter Command: ").lower()

    # ---------- DEPOSIT ----------
    if user_command == "deposit money" or user_command == "1":
        money_to_deposit = float(input("How much money do you want to deposit: "))

        if money_to_deposit <= 0:
            print("Deposit amount must be positive!")
        else:
            bank_balance += money_to_deposit
            print(f"Now your bank balance is: {bank_balance}")

    # ---------- WITHDRAW ----------
    elif user_command == "withdraw money" or user_command == "2":
        money_to_withdraw = float(input("How much money do you want to withdraw: "))

        if money_to_withdraw <= 0:
            print("Withdraw amount must be positive!")
        elif money_to_withdraw > bank_balance:
            print("You can't withdraw more money than you have!")
        else:
            bank_balance -= money_to_withdraw
            print(f"Now your bank balance is: {bank_balance}")

    # ---------- EXIT ----------
    elif user_command == "exit" or user_command == "3":
        pincode = input("Enter your pincode: ")

        if pincode == user_pin:
            print("Bye 👋")
            break
        else:
            print("Initializing self destruct...")
            time.sleep(0.5)
            print("3")
            time.sleep(0.5)
            print("2")
            time.sleep(0.5)
            print("1")
            time.sleep(0.5)
            print("💥 BOOM!")
            time.sleep(0.5)
            break

    # ---------- INVALID COMMAND ---------- #
    else:
        print("Invalid command! Please choose 1, 2, or 3.")
