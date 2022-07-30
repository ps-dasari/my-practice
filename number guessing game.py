#number guessing game
from random import *
import sys
class no_arg_given(Exception):
    def __init__(self,arg):
        self.msg=arg
x=int(input('first number='))
y=int(input('second number='))
if x>y:
    print('y should be grater than x')
else:
    print('you have five chances to guess a number from {} to {}'.format(x,y))
rang=list(range(x,y+1))
guss=randint(x,y)
for i in range(1,7):
        guess_number = int(input('guess number='))
        if guess_number in rang:
            if guess_number==guss:
                print('''--wow-- ,
                    correct guess:)''')
                sys.exit()
            elif guess_number>guss:
                if i + 1 == 6:
                    print('incorrect')
                    print('--out of chances--')
                    print('better luck next time')
                    sys.exit()
                else:
                    print('incorrect')
                    print('{} chance'.format(i + 1))
                    print('try with a smaller number')

            elif guess_number<guss:
                if i + 1 == 6:
                    print('incorrect')
                    print('--out of chances--')
                    print('better luck next time')
                    sys.exit()
                else:
                    print('incorrect')
                    print('{} chance'.format(i + 1))
                    print('try with a larger number')
        else:
            raise no_arg_given('''out of range
                    --invalid number--''')




