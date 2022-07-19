import random
import sys
from random import *
balance = float(input('balance='))
notes=int(input('notes='))
def bank():
    name = 'ps'
    idnumber=1010
    global balance
    global notes
    print('welcome {} chose one option'.format(name))
    print('''1:diposit\n2:withdral\n3:checkbalance\n4:exit\n5:change pin''')
    option=input('option=')
    if option=='1':
        deposit=float(input('deposit amount='))
        denomination = (deposit if deposit% 100 == 0 else print('only 100s or 200s or 500s or 2000 notes'))
        if deposit==(denomination):
            balance=balance+deposit
            print('total balance:',balance)
            print('transaction complete')
            bank()
        else:bank()
    elif option=='2':
        withdraw_amount=float(input('withdraw amount='))
        amount=(withdraw_amount if withdraw_amount% 100==0 else print('only 100s or 200s or 500s or 2000 notes'))
        if amount>=balance:
                    print('in sufficent funds')
        elif amount<balance:
            if amount%notes!=0:
                print('give amount in the multiple of {}'.format(notes))
                sys.exit()
            else:
                print('collect {} of {}X{} notes'.format(amount,amount/notes,notes))
                balance=balance-withdraw_amount
                print('your prasent balance:',balance)
    elif option=='3':
        print('your account balance:',balance)
    elif option==4:
        print('thank you {}'.format(name))
        sys.exit()
    elif option=='5':
        print('you have chosen to change the pin')
        print('for confermation print yes/no')
        z=input()
        if z=='yes':
            yes=[]
            for i in range(6):
                l1=randrange(0,9,1)
                yes.append(l1)
            print(yes)
            no=[]
            for i in range(6):
                x=int(input())
                no.append(x)
                print()
            print(no)
            if yes==no:
                print('succesfully done')
            else:
                print('transaction decline')
                sys.exit()
        else:
            sys.exit()




b=bank()
