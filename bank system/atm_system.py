import csv


class Account:
    accounts = []

    def __init__(self, name, password, acno, balance, pin):
        self.name = name
        self.password = password
        self.acno = acno
        self.balance = int(balance)
        self.pin = pin
        Account.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > int(self.balance):
            print("Insufficient funds")
        else:
            self.balance -= amount

    def check_balance(self):
        print(f"Your balance is : {self.balance}Rs ")

    @classmethod
    def pin_verification(cls, pin):
        for account in cls.accounts:
            if account.name and account.pin == pin:
                return True
            else:
                return None

    @classmethod
    def login(cls, name, password, acno):
        for account in cls.accounts:
            if account.name == name and account.password == password:
                return account
            elif account.acno == acno and account.password == password:
                return account
        return None


def accounts_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            account = Account(row['name'], row['password'], row['acno'], row['balance'], row['pin'])
            Account.accounts.append(account)


def enter_pin():
    pin = input("Enter pin : ")
    pin = Account.pin_verification(pin)
    if pin:
        return pin
    else:
        print("wrong pin")
        return None


def user_login():
    name = input("Enter name : ")
    acno = input("Enter account number : ")
    password = input("Enter password : ")
    account = Account.login(name,password,acno)
    if account:
        return account
    else:
        print("Invalid credentials")
        return None


def banking_system():
    account = user_login()
    if account:
        print(f"welcome {account.name}")
        while True:
            print("\n 1.withdraw money : ")
            print("   2.deposit money : ")
            print("   3.check balance : ")
            print("   4.log out : ")

            choice = int(input("\nEnter your choice : "))
            if choice == 1:
                amount = int(input("Enter amount to withdraw : "))
                pin = enter_pin()
                if pin:
                    account.withdraw(amount)
                    print(f"withdrawal successfully done!!\n current balance : {account.balance}Rs ")

            elif choice == 2:
                amount = int(input("Enter amount to deposit : "))
                pin = enter_pin()
                if pin:
                    account.deposit(amount)
                    print(f"deposition successfully done!!\n current balance : {account.balance}Rs ")

            elif choice == 3:
                pin = enter_pin()
                if pin:
                    account.check_balance()

            elif choice == 4:
                print("Logging out.")
                break
            else:
                print("Invalid choice.")


accounts_from_csv('accounts.csv')

banking_system()



