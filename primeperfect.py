# x=int(input('x='))
#
# if x>1:
#     for i in list(range(2,x)):
#         if (x%i==0):
#             print(x,"its not a prime number")
#             break
#         else:print((x,"prime number"))

x=int(input('x='))
if x>1:
    for i in range(2, x):
        if (x%i==0):
             print('%i is not a prime number' %x)
             break
    else:print('%i is a prime number' %x)
else:print('%i is not a valide number' %x)

print()
print()

for num in range(100, 300 + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=' ;')

