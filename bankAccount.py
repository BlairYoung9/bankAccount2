class BankAccount:
        
        def __init__(self, int_rate=0.01, balance=0):
                self.int_rate = int_rate
                self.balance = balance

        def deposit(self, amount):
                self.balance += amount
                return self

        def withdraw(self, amount):
                self.balance -= amount
                return self

        def display_account_info(self):
                print(self.balance)
                return self

        def yield_interest(self):
                self.balance += self.balance * self.int_rate
                return self

blair = BankAccount(.10, 10000)
bob = BankAccount(.05, 5000)

blair.deposit(100).deposit(200).deposit(300).withdraw(500).yield_interest().display_account_info()
bob.deposit(200).deposit(300).withdraw(100).withdraw(200).withdraw(300).withdraw(400).yield_interest().display_account_info()

