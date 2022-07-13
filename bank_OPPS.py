import sys


class bank:
    x='businessbank'
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print('balance after deposit',self.balance)
    def withdral(self,amount):
        if amount>self.balance:
            print('insuffecent funds')
            sys.exit()
        else:
            self.balance=self.balance-amount
            print('balance after withdral:',self.balance)
print('welcome to',bank.x)
name=input('name=')
b=bank(name)
while True:
    print('d-deposit \nw-withdral \ne-exit')
    option=input('chose one option=')
    if (option=='d') or (option=='D'):
        amount=float(input('amount='))
        b.deposit(amount)
    elif (option=='w') or (option=='W'):
        amount=float(input('amount='))
        b.withdral(amount)
    elif (option=='e') or (option=='W'):
        print('Thanks for banking')
    else:
        print('invalid option')
        sys.exit()





