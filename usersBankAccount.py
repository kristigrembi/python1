class BankAccount:
    accounts = {}
    def __init__(self, name,  balance=0): 
        self.name= name
        BankAccount.accounts[self.name] = 0
        self.balance=balance
    def deposit(self, amount):
        BankAccount.accounts[self.name] += amount
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance-amount>0:
            self.balance-=amount
            print('Your balance is now: ' + str(self.balance))
        else:
            print('Insuficent Funds') 
        return self
    def display_account_info(self):
        print('Your balance is : ' + str(self.balance))


account = BankAccount('adrien')
account.deposit(1000)
print(BankAccount.accounts)