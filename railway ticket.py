def display_menu():
    print("\n=== Railway Ticket System ===")
    print("1. Book Ticket")
    print("2. Exit")

def book_ticket():
    name = input("Enter passenger name: ")
    destination = input("Enter destination: ")
    try:
        num_tickets = int(input("Enter number of tickets: "))
        fare_per_ticket = 150  # Fixed fare
        total_fare = fare_per_ticket * num_tickets

        print("\n--- Ticket Summary ---")
        print(f"Passenger Name : {name}")
        print(f"Destination    : {destination}")
        print(f"Tickets        : {num_tickets}")
        print(f"Total Fare     : ₹{total_fare}")
    except ValueError:
        print("Invalid input for number of tickets.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            book_ticket()
        elif choice == '2':
            print("Thank you for using the Railway Ticket System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
