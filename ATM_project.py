class ATM:
    def __init__(self, bank_name, location, balance):
        self.bank_name = bank_name
        self.location = location
        self.balance = balance

    def credit(self):
        try:
            amount = float(input("Enter amount to credit: "))
            if amount <= 0:
                print("Please enter a positive amount.")
            else:
                self.balance += amount
                print(f"${amount:.2f} credited to your account.")
                print(f"Your current balance is: ${self.balance:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def debit(self):
        try:
            amount = float(input("Enter amount to debit: "))
            if amount <= 0:
                print("Please enter a positive amount.")
            elif amount > self.balance:
                print("Insufficient balance.")
            else:
                self.balance -= amount
                print(f"${amount:.2f} debited from your account.")
                print(f"Your current balance is: ${self.balance:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def show_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def display_menu(self):
        print("\nATM Menu:")
        print("1. Credit")
        print("2. Debit")
        print("3. Balance")
        print("4. Exit")

    def get_choice(self):
        return input("Enter your choice (1-4): ")

    def main(self):
        while True:
            self.display_menu()
            choice = self.get_choice()

            if choice == '1':
                self.credit()
            elif choice == '2':
                self.debit()
            elif choice == '3':
                self.show_balance()
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Example usage
raju_account = ATM('SBI', 'Hyderabad', 10000)
raju_account.main()
