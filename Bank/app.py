from flask import Flask, send_from_directory
import click
import os

app = Flask(__name__)


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ₹{amount}")
            print(f"New balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Successfully withdrew ₹{amount}")
            print(f"Remaining balance: ₹{self.balance}")

    def display_balance(self):
        print(f"\nAccount Holder: {self.holder}")
        print(f"Current Balance: ₹{self.balance}")


def main():
    print("----- Welcome to Python Central Bank -----")
    name = input("Enter your name to open an account: ")

    user_account = BankAccount(name)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == '1':
            amt = float(input("Enter deposit amount: "))
            user_account.deposit(amt)

        elif choice == '2':
            amt = float(input("Enter withdrawal amount: "))
            user_account.withdraw(amt)

        elif choice == '3':
            user_account.display_balance()

        elif choice == '4':
            print("Thank you for banking with us!")
            break

        else:
            print("Invalid choice!")

            

if __name__ == '__main__':
    app.run()
