from abc import ABC, abstractmethod


# Abstract 
class BankAccount(ABC):

    def __init__(self, account_number, customer_name, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful.")
        else:
            print("Invalid deposit amount.")

    def get_balance(self):
        return self.__balance

    def show_account(self):
        print("Account Number:", self.account_number)
        print("Customer Name:", self.customer_name)
        print("Balance:", self.__balance)

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):

    def withdraw(self, amount):
        if amount <= self.get_balance():
            self._BankAccount__balance -= amount
            print("Savings account withdrawal successful.")
        else:
            print("Insufficient balance.")

    def calculate_interest(self):
        interest = self.get_balance() * 0.05
        print("Savings Account Interest:", interest)

class CurrentAccount(BankAccount):

    def withdraw(self, amount):
        charge = 100

        if amount + charge <= self.get_balance():
            self._BankAccount__balance -= (amount + charge)
            print("Current account withdrawal successful.")
            print("Transaction charge:", charge)
        else:
            print("Insufficient balance.")

    def calculate_interest(self):
        print("Current accounts do not receive interest.")

class FixedDepositAccount(BankAccount):

    def withdraw(self, amount):
        print("Withdrawal is not allowed from a fixed deposit account.")

    def calculate_interest(self):
        interest = self.get_balance() * 0.08
        print("Fixed Deposit Interest:", interest)


# objects
savings = SavingsAccount("S001", "Kamal", 100000)
current = CurrentAccount("C001", "Nimal", 100000)
fixed = FixedDepositAccount("F001", "Sunil", 200000)



print("\n--- Savings Account ---")
savings.show_account()
savings.deposit(10000)
savings.withdraw(20000)
savings.calculate_interest()
print("Final Balance:", savings.get_balance())


print("\n--- Current Account ---")
current.show_account()
current.deposit(10000)
current.withdraw(20000)
current.calculate_interest()
print("Final Balance:", current.get_balance())


print("\n--- Fixed Deposit Account ---")
fixed.show_account()
fixed.deposit(10000)
fixed.withdraw(20000)
fixed.calculate_interest()
print("Final Balance:", fixed.get_balance())