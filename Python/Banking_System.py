# -----------------------------
# Parent Class
# -----------------------------
class Person:

    def __init__(self, name):
        self.name = name


# -----------------------------
# Child Class
# -----------------------------
class BankAccount(Person):

    # Class Variable
    bank_name = "State Bank of India"

    def __init__(self, name, account_number, balance):
        super().__init__(name)

        self.account_number = account_number
        self._balance = balance          # Protected Variable
        self.__pin = "1234"              # Private Variable

    # Deposit Money
    def deposit(self, amount):
        self._balance += amount
        print(f"₹{amount} Deposited Successfully.")

    # Withdraw Money
    def withdraw(self, amount, pin):

        if pin != self.__pin:
            print("Incorrect PIN")
            return

        if amount > self._balance:
            print("Insufficient Balance")

        else:
            self._balance -= amount
            print(f"₹{amount} Withdrawn Successfully.")

    # Display Account
    def display(self):
        print("\n----- Account Details -----")
        print("Name:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self._balance)

    # Class Method
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    # Static Method
    @staticmethod
    def validate_pin(pin):
        return len(pin) == 4 and pin.isdigit()


# -----------------------------
# Main Program
# -----------------------------
account = BankAccount("Ram", 1001, 5000)

while True:

    print("\n===== Banking System =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Account")
    print("4. Change Bank Name")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        amount = float(input("Enter Amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter Amount: "))
        pin = input("Enter PIN: ")

        if BankAccount.validate_pin(pin):
            account.withdraw(amount, pin)
        else:
            print("PIN must contain exactly 4 digits.")

    elif choice == "3":
        print("Bank:", BankAccount.bank_name)
        account.display()

    elif choice == "4":
        name = input("Enter New Bank Name: ")
        BankAccount.change_bank_name(name)
        print("Bank Name Updated.")

    elif choice == "5":
        break

    else:
        print("Invalid Choice")