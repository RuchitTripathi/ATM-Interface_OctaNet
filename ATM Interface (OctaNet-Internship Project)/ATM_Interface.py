import datetime

class User:
    def __init__(self, user_id, pin, name, balance):
        self.user_id = user_id
        self.pin = pin
        self.name = name
        self.balance = balance

    def display_user_info(self):
        print(f"User ID: {self.user_id}")
        print(f"Name: {self.name}")
        print(f"Balance: ${self.balance:.2f}")

class Account:
    def __init__(self, user):
        self.user = user
        self.transaction_history = []

    def add_transaction(self, transaction_type, amount):
        transaction = Transaction(transaction_type, amount)
        self.transaction_history.append(transaction)

    def display_balance(self):
        print(f"Your current balance is: ${self.user.balance:.2f}")

    def display_transaction_history(self):
        for transaction in self.transaction_history:
            transaction.display_transaction()

class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        self.transaction_type = transaction_type
        self.amount = amount
        self.date = datetime.datetime.now()

    def display_transaction(self):
        print(f"Transaction ID: {self.transaction_id}")
        print(f"Type: {self.transaction_type}")
        print(f"Amount: ${self.amount:.2f}")
        print(f"Date: {self.date.strftime('%Y-%m-%d %H:%M:%S')}")

class ATM:
    def __init__(self):
        # Assume I have some predefined user accounts
        self.users = {
            "user1": User("user1", "123", "Ram", 100000.0),
            "user2": User("user2", "456", "Shyam", 150000.0),
            "user3": User("user3", "789", "Ruchit", 50000.0)
        }

    def check_credentials(self, user_id, pin):
        user = self.users.get(user_id)
        if user and user.pin == pin:
            return True
        return False

    def get_user(self, user_id):
        return self.users.get(user_id)

    def display_menu(self):
        print("\nMain Menu:")
        print("1. Display Transaction History")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Logout")
        print("Type 'quit' to exit")
        choice = input("Please select an option: ")
        return choice
    
    def display_transaction_history(self, user):
        user_account = Account(user)
        user_account.display_transaction_history()

class App:
    def __init__(self):
        self.atm = ATM()
        self.user = None

    def run(self):
        while True:
            if not self.user:
                user_id = input("Enter User ID: ")
                pin = input("Enter PIN: ")
                if self.atm.check_credentials(user_id, pin):
                    self.user = self.atm.get_user(user_id)
                else:
                    print("Invalid credentials. Please try again.")
            else:
                choice = self.atm.display_menu()
                if choice == "1":
                    self.atm.display_transaction_history(self.user)
                elif choice == "2":
                    self.process_withdrawal(self.user)
                elif choice == "3":
                    self.process_deposit(self.user)
                elif choice == "4":
                    self.process_transfer(self.user)
                elif choice == "5":
                    self.user = None  # Logout
                elif choice.lower() == "quit":
                    break

    def process_withdrawal(self, user):
        try:
            amount = float(input("Enter the withdrawal amount: $"))
            if amount <= 0 or amount > user.balance:
                print("Invalid amount. Please try again.")
            else:
                user.balance -= amount
                user_account = Account(user)
                user_account.add_transaction("Withdrawal", amount)
                user_account.display_balance()
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def process_deposit(self, user):
        try:
            amount = float(input("Enter the deposit amount: $"))
            if amount <= 0:
                print("Invalid amount. Please try again.")
            else:
                user.balance += amount
                user_account = Account(user)
                user_account.add_transaction("Deposit", amount)
                user_account.display_balance()
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def process_transfer(self, user):
        try:
            recipient_id = input("Enter the recipient's User ID: ")
            recipient = self.atm.get_user(recipient_id)
            if recipient is None:
                print("Recipient not found. Please try again.")
                return

            amount = float(input("Enter the transfer amount: $"))
            if amount <= 0 or amount > user.balance:
                print("Invalid amount. Please try again.")
            else:
                user.balance -= amount
                recipient.balance += amount

                sender_account = Account(user)
                sender_account.add_transaction("Transfer to " + recipient_id, amount)

                recipient_account = Account(recipient)
                recipient_account.add_transaction("Transfer from " + user.user_id, amount)

                user_account = Account(user)
                user_account.display_balance()
        except ValueError:
            print("Invalid input. Please enter a valid amount.")


if __name__ == "__main__":
    app = App()
    app.run()