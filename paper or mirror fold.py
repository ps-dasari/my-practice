def decor(func):
    x = [0,['Abhi', 'Bobi', 'Cobi', 'Dobi', 'Eobi'],
         1,['Fog', 'Gog', 'Hog', 'Iog'  ,    'Jog'],
         2,['Kill', 'Lill', 'Mill', 'Nill', 'Oill'],
         3,['Pir', 'Qir', 'Rir', 'Sir',      'Tir']]
    for i in x:
        print(i,sep='     ')
    def nice(line,name):
        print('we can also call this programm as mirror images')
        return func(line,name)
    return nice
@decor
def paper(line,name):

    if line>3 or name>4:
        print('not in range give correct value based on x')
    else:
        x = [['Abhi', 'Bobi', 'Cobi', 'Dobi', 'Eobi'],
             ['Fog', 'Gog', 'Hog', 'Iog', 'Jog'     ],
             ['Kill', 'Lill', 'Mill', 'Nill', 'Oill'],
             ['Pir', 'Qir', 'Rir', 'Sir', 'Tir'     ]]
        what=x[line][name]
        print(what)
        print(x[line][name-1])
        for x[line][name] in x:
            print(x[line][name+1])
            print(x[line][name+2])
            break
        return what
paper(int(input('which row=')),int(input('which colome=')))




