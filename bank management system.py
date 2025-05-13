# Dictionary to store account details
account = {}

def display_menu():
    print("\n=== Bank Management System ===")
    print("1. Create Account")
    print("2. Withdraw Money")
    print("3. Exit")

def create_account():
    if account:
        print("Account already exists!")
        return
    name = input("Enter your name: ")
    try:
        balance = float(input("Enter initial deposit amount: ₹"))
        account['name'] = name
        account['balance'] = balance
        print(f"Account created for {name} with ₹{balance:.2f}")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def withdraw_money():
    if not account:
        print("No account found. Please create one first.")
        return
    try:
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > account['balance']:
            print("Insufficient balance.")
        else:
            account['balance'] -= amount
            print(f"Withdrawal successful. Remaining balance: ₹{account['balance']:.2f}")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            create_account()
        elif choice == '2':
            withdraw_money()
        elif choice == '3':
            print("Thank you for using the Bank Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
