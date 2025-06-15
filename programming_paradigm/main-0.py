import sys
import os
from bank_account import BankAccount

BALANCE_FILE = "balance.txt"

def read_balance():
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "r") as f:
            return float(f.read())
    return 100.0  # Default initial balance

def save_balance(account):
    # Access the private variable using name mangling
    with open(BALANCE_FILE, "w") as f:
        f.write(str(account._BankAccount__account_balance))

def main():
    account = BankAccount(read_balance())  # Reads saved balance or uses 100

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        save_balance(account)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            save_balance(account)
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
