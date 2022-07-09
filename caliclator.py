x=a,b=(int(x) for x in input('give two inputs').split('.'))
functions={1:'add',2:'sub',3:'mul',4:'div'}
print(functions)
add = a + b
sub = a - b
mul = a * b
div = a / b
for y in ['1','2','3','4']:
    y = int(input('y='))
    if y==1:
          print(add)
          break
    elif y==2:
        print(sub)
        break
    elif y==3:
        print(mul)
        break
    elif y==4:
         print(div)
         break
