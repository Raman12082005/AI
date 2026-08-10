import json
def save_data():
    data = []
    for acc in accounts:
        data.append(acc.to_dict())
    with open("banking.json", "w") as file:
        json.dump(data, file, indent=4)
def load_data():
    try:
        with open("banking.json", "r") as file:
            data = json.load(file)
            for item in data:
                accounts.append(banking_system(item["name"], item["acc_no"], item["balance"]))
    except (FileNotFoundError, json.JSONDecodeError):
        pass


class banking_system:
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
    def display(self):
        print("Account No.: ", self.acc_no)
        print("Account Holder Name : ", self.name)
        print("Account Balance : ", self.balance)
    def to_dict(self):
        return{
            "name" : self.name,
            "acc_no" : self.acc_no,
            "balance" : self.balance

        }

accounts = []
load_data()
while True:
    print("1. Create Account")
    print("2.Show all Accounts")
    print("3. Deposite Money")
    print("4. Check balance")
    print("5. Withdraw")
    print("6. Search a Account")
    print("7. Delete a Account")
    print("8. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        acc_no = int(input("Enter Acc. No.: "))
        found = False
        for acc in accounts:
            if acc.acc_no == acc_no:
                print("This account no. is already Taken, please try another one")
                found = True
                break
        if found:
            continue

        name = input("Enter Holder's name: ")
        balance = int(input("Enter Your Balance: "))

        accounts.append(banking_system(name, acc_no, balance))
        save_data()

    elif choice == "2":
        if(len(accounts) == 0):
            print("No Account found")
        else:
            print("**________data of Accounts_________**")
            for acc in accounts:
                acc.display()
                print("--------------------")

    elif choice == "3":
        if(len(accounts) == 0):
            print("No Account Exist")
        else:
            no = int(input("Enter Acc. No.: "))
            amount = int(input("Enter the ammount: "))
            found = False
            for acc in accounts:
                if(acc.acc_no == no):
                    if amount > 0:
                        acc.balance += amount
                        print("Deposite Successfull")
                        print("New balance = ", acc.balance)
                        save_data()
                    else:
                        print("Amount must be greater than 0")

                    found = True
                    break
            if not found:
                print("No Account found")

    elif(choice == "4"):
        no = int(input("Enter Acc. No.: "))
        found = False
        for acc in accounts:
            if acc.acc_no == no:
                acc.display()
                found = True
                break
        if not found:
            print("No Account Found")

    elif choice == "5":
        amount = int(input("Enter Amount: "))
        if(amount <= 0):
            print("Enter amount greater than 0")
        else:
            no = int(input("Enter Acc. no.: "))
            found = False
            for acc in accounts:
                if acc.acc_no == no:
                    found = True
                    if acc.balance < amount:
                        print("Insufficient Balance")
                    else:
                        acc.balance -= amount
                        print("Withdraw Sucessfull")
                        save_data()
                        break    
            if not found:
                print("No Account found")

    elif choice == "6":
        if len(accounts) == 0:
            print("No Account found")
        else:
            no = int(input("Emter Account No.: "))
            found = False
            for acc in accounts:
                if acc.acc_no == no:
                    print("--------Displaying account Details---------")
                    acc.display()
                    found = True
                    break
            if not found:
                print("Account not Found")

    elif choice == "7":
        if len(accounts) == 0:
            print("No Account found: ")
        else:
            no = int(input("Enter Account no.: "))
            found = False
            for acc in accounts:
                if acc.acc_no == no:
                    print("-------Account deleted Successfully------")
                    accounts.remove(acc)
                    save_data()
                    found = True
                    break
            if not found:
                print("No account Found")
                


    elif(choice == "8"):
        break

    else:
        print("Invalid choice. Please try again")

        
