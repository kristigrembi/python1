class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance=0): 
        self.interest_rate= int_rate
        self.balance=balance
    def deposit(self, amount):
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
        
    def yield_interest(self):
        if self.balance>0:
            self.balance *= self.int_rate
        return self
banka1 = BankAccount(0.2)
print(banka1.balance)
banka1.deposit(1000)
print(banka1.balance)

banka1.withdraw(500)