from flask import Flask
import click

app = Flask(__name__)

class BankAccount:
    
    def __init__(self, name, account_number, initial_balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True, f"✅ Deposited ₹{amount:.2f}. New Balance: ₹{self.balance:.2f}"
        return False, "❌ Deposit amount must be greater than zero"
    
    def withdraw(self, amount):
        if amount <= 0:
            return False, "❌ Withdrawal amount must be greater than zero"
        elif amount > self.balance:
            return False, f"❌ Insufficient balance. Available: ₹{self.balance:.2f}"
        else:
            self.balance -= amount
            return True, f"✅ Withdrew ₹{amount:.2f}. Remaining Balance: ₹{self.balance:.2f}"
    
    def get_balance(self):
        return self.balance

accounts = {}

@app.cli.command()
@click.argument('name')
@click.argument('account_number')
@click.option('--initial', default=0.0, help='Initial deposit amount')
def create(name, account_number, initial):
    if account_number in accounts:
        click.echo(f"❌ Account {account_number} already exists!")
        return
    
    accounts[account_number] = BankAccount(name, account_number, initial)
    click.echo(f"\n✅ Account created successfully!")
    click.echo(f"Name: {name}")
    click.echo(f"Account Number: {account_number}")
    click.echo(f"Initial Balance: ₹{initial:.2f}\n")

@app.cli.command()
@click.argument('account_number')
@click.argument('amount', type=float)
def deposit(account_number, amount):
    if account_number not in accounts:
        click.echo(f"❌ Account {account_number} not found!")
        return
    
    success, message = accounts[account_number].deposit(amount)
    click.echo(f"\n{message}\n")

@app.cli.command()
@click.argument('account_number')
@click.argument('amount', type=float)
def withdraw(account_number, amount):
    if account_number not in accounts:
        click.echo(f"❌ Account {account_number} not found!")
        return
    
    success, message = accounts[account_number].withdraw(amount)
    click.echo(f"\n{message}\n")

@app.cli.command()
@click.argument('account_number')
def balance(account_number):
    if account_number not in accounts:
        click.echo(f"❌ Account {account_number} not found!")
        return
    
    acc = accounts[account_number]
    click.echo(f"\n💰 Account Balance")
    click.echo(f"Name: {acc.name}")
    click.echo(f"Account Number: {acc.account_number}")
    click.echo(f"Current Balance: ₹{acc.balance:.2f}\n")

@app.cli.command()
def interactive():
    click.echo("=" * 50)
    click.echo("🏦 BANK ACCOUNT MANAGEMENT SYSTEM 🏦")
    click.echo("=" * 50)
    
    name = click.prompt("\nEnter Account Holder Name")
    account_number = click.prompt("Enter Account Number")
    initial_balance = click.prompt("Enter Initial Deposit (or 0)", type=float, default=0.0)
    
    account = BankAccount(name, account_number, initial_balance)
    click.echo(f"\n✅ Account created successfully for {name}!")
    click.echo(f"Account Number: {account_number}")
    click.echo(f"Initial Balance: ₹{initial_balance:.2f}\n")
    
    while True:
        click.echo("=" * 50)
        click.echo("MENU OPTIONS")
        click.echo("=" * 50)
        click.echo("1. Deposit Money")
        click.echo("2. Withdraw Money")
        click.echo("3. Check Balance")
        click.echo("4. Exit")
        click.echo("=" * 50)
        
        choice = click.prompt("\nEnter your choice (1-4)", type=str)
        
        if choice == '1':
            amount = click.prompt("Enter amount to deposit", type=float)
            success, message = account.deposit(amount)
            click.echo(f"\n{message}\n")
        
        elif choice == '2':
            amount = click.prompt("Enter amount to withdraw", type=float)
            success, message = account.withdraw(amount)
            click.echo(f"\n{message}\n")
        
        elif choice == '3':
            click.echo(f"\n💰 Account Balance for {account.name}")
            click.echo(f"Account Number: {account.account_number}")
            click.echo(f"Current Balance: ₹{account.balance:.2f}\n")
        
        elif choice == '4':
            click.echo("\n" + "=" * 50)
            click.echo("Thank you for using our Bank Account System!")
            click.echo(f"Final Balance: ₹{account.balance:.2f}")
            click.echo("=" * 50)
            click.echo("Goodbye! 👋\n")
            break
        
        else:
            click.echo("\n❌ Invalid choice! Please select 1-4.\n")

if __name__ == '__main__':
    app.run()
