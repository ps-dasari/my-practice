import random
import sys
from random import *
ATM_BALANCE=100000

balance = 50000#float(input('balance='))

class invalid_note(Exception):
    def __init__(self,arg):
        self.arg=arg
class invalid_option(Exception):
    def __init__(self, arg):
        self.msg = arg
class pin_changer(Exception):
    def __init__(self, arg):
        self.msg = arg
print('cash in 100,200,500,2000')
notes = int(input('notes='))
if notes not in [100,200,500,2000]:
    raise invalid_note('invalid notes')
pin_count=1
def bank():
    name ='ps'#input('name=')
    idnumber='963852741' #input('acc no=')
    def security():
        global pin_count
        pin=input('4 digit pin number=')
        count=0
        for i in pin:
            if i.isdecimal():
                count+=1
            else:print('invalid pin number')
        if count!=4:
            print('incorrect pin')
            print('Re-entir your pin')
            print('only {} attempts left'.format(3 - pin_count))
            pin_count += 1
            if pin_count > 3:
                    print('sorry,your account has blocked')
                    print('consult your bank')
                    sys.exit()
            security()
    security()
    if len(idnumber)!=9:
        print('incorrect acc number')
        print('please check the number')
        sys.exit()
    global balance
    global notes
    global ATM_BALANCE
    print('welcome {} chose one option'.format(name))
    print('''1:diposit\n2:withdral\n3:checkbalance\n4:exit\n5:change pin''')
    option=input('option=')
    if option=='1':
        deposit=float(input('deposit amount='))
        denomination = (deposit if deposit% 100 == 0 else print('only 100s or 200s or 500s or 2000 notes'))
        if deposit==(denomination):
            balance=balance+deposit
            ATM_BALANCE=ATM_BALANCE+deposit
            print(ATM_BALANCE,'donkey')
            print('total balance:',balance)
            print('transaction complete')
            bank()
        else:bank()
    elif option=='2':
        withdraw_amount=float(input('withdraw amount='))
        amount=(withdraw_amount if withdraw_amount% 100==0 else print('only 100s or 200s or 500s or 2000 notes'))
        if type(amount)!=type(withdraw_amount):
            print('diclined transaction')
            sys.exit()
        if withdraw_amount>balance:
            print('in sufficent funds')
        elif withdraw_amount<balance:
            if amount%notes!=0:
                print('only in {}'.format(notes))
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
        z=input('')
        if z in ['yes','no','YES','NO']:
            print('processing..')
        else:
            raise pin_changer('invalid option')
        if (z=='yes') or(z== 'YES'):
            print('your OTP')
            yes=[]
            for i in range(6):
                l1=randrange(0,9,1)
                yes.append(l1)
            print(yes)
            otp=[]
            print('enter OTP')
            for i in range(6):
                x=int(input())
                otp.append(x)
                print()
            print(otp)
            if yes==otp:
                print('succesfully done')
            else:
                print('transaction decline')
                sys.exit()
        else:# z=='no':
            print('thankyou for chosing our bank')
            sys.exit()
    else:
        raise invalid_option('invalid option')

print('thank you for chosing our bank')
b=bank()
