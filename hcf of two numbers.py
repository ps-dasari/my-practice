x=a,b=(int(x) for x in input('give two numbers a,b=').split(','))
if a>b:
    smaller=b
    print('%i is the smaller number' %b)
else:
    smaller=a
    print('%i is the smaller number' %a)

for i in range(smaller+1,2,-1):
    if (a%i==0) and (b%i==0):
        hcf=i
        print("hcf is",i)
        break
        



# for i in range(0,x+1):
#     for j in range(0,i):
#           print('p',end='')
#     print()
