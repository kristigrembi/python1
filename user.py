class User:
    # class attributes get defined in the class 
    bank_name = "First National Dojo"
    # now our method has 2 parameters!
    def __init__(self, name, email_address , balance=0):
        self.name = name
        self.email = email_address
        self.balance=balance
    def deposit(self, amount):
        self.balance += amount
        return self   
    def withdraw(self, amount):
        if self.balance-amount>0:
            self.balance-=amount
        else:
            print('Insuficent Funds') 
        return self
    def display_account_info(self):
        print('Your balance is : ' + str(self.balance))
guido = User("User: Guido, Balance: ", "guido@python.com")
monty = User("User: Monty, Balance: ", "monty@python.com")
guido.deposit(3645)
monty.deposit(2440)
monty.withdraw(175)
guido.withdraw(84)
print(guido.name, guido.balance)
print(monty.name, monty.balance)
