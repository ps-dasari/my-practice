x=int(input('x='))
sum=0
for i in range(0,x):
    sum=sum+i
    print(sum,end=',')


print()
print('................................................................................................................')
print()

# x=int(input('x='))
sum,i=0,0
while i<x:
    sum=sum+i
    i+=1
    print(sum,end=",")
