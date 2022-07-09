def dec(func):
    def inner():
        x=func()
        print('111111111111111111111')
        print(x)
        return x*x
    return inner
def dec1(func):
    def inner():
        x=func()
        print(x)
        print('222222222222222222222')
        return 2*x
    return inner
@dec
@dec1
def num():
    return 10
print(num())
