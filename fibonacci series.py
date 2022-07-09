x=int(input('x='))
y,z=0,1
fib=0
if x<=0:
      print('please enter a +ve intiger')
elif x==1:
      print('fibonacci series is %i' %y)
else:
      while fib<x:
            fib=y+z
            y=z
            z=fib
            x+=1
            print(fib)


