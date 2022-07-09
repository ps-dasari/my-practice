x=a,b=(int(x) for x in input('x numbers=').split(','))
y=c,d=(int(y) for y in input('y numbers=').split(','))
p=e,f=(int(y) for y in input('p numbers=').split(','))
q=m,n=(int(y) for y in input('q numbers=').split(','))
# #y=int(input('y='))
count=0
for i in [c,d]:
    if count<1:
        for j in [a,b]:
            print(j,end=',')
            count+=1
        print()
    print(i,end=',')
print()
count=0
for i in [m,n]:
    if count<1:
        for j in [e,f]:
            print(j,end=',')
            count+=1
        print()
    print(i,end=',')
print()
print("sum of matrix is")
print()
count=0
for i in [c+m,d+n]:
    if count<1:
        for j in [a+e,b+f]:
            print(j,end=',')
            count+=1
        print()
    print(i,end=',')
print()






