from random import *
from time import *
def d1():
    global n
    print('''its free and any one can join
     **FACEBOOK**''')
    member=input('do you have an account[yes]/[no]=')
    if member=='yes':
        username=input('username:')
        mobilenumber=int(input('mobilenumber:'))
        if len(str(mobilenumber))==10:
            print('checking your details...')
        else:
            print('''invalid number
                        give 10 digit number''')
            d1()
        sleep(5)
        print('your OTP is')
        m=0
        box=[]
        while m<4:
            n=randint(1,9)
            box.append(n)
            m+=1
        print(box)
        pox=[]
        a=0
        while a<4:
            OTP = int(input('OTP digit wise=>'))
            pox.append(OTP)
            a+=1
        if pox == box:
                print('hello',username)
                print('after a long time')
                print('how are you')
        else:print('incorrect otp')
    else:
        print('creat new account')
        print('SIGNUP.?')
        firstname=input('firstname=')
        lastname=input('lastname=')
        i_am=input('sex.?[male][female][dont want to say]')
        dateofbirth=('date of bith')
        signup=input('creating a new face book account:[yes]/[no]=')
        if signup=='yes':
            print('hello',firstname+' '+lastname)
            print('''welcome to facebook
            facebook helps you to connect and share with the people in your life.''')
        elif signup=='no':
            print('may be some time later')


d1()




