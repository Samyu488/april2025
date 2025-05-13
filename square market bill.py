def display_menu():
    print("\n=== Supermarket Menu ===")
    print("1. Rice - ₹50/kg")
    print("2. Sugar - ₹40/kg")
    print("3. Exit")

def main():
    total_bill = 0
    prices = {
        "rice": 50,
        "sugar": 40
    }

    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            qty = float(input("Enter quantity of rice (in kg): "))
            cost = qty * prices["rice"]
            total_bill += cost
            print(f"Added Rice - ₹{cost:.2f}")
        elif choice == '2':
            qty = float(input("Enter quantity of sugar (in kg): "))
            cost = qty * prices["sugar"]
            total_bill += cost
            print(f"Added Sugar - ₹{cost:.2f}")
        elif choice == '3':
            print(f"\nTotal Bill: ₹{total_bill:.2f}")
            print("Thank you for shopping!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
