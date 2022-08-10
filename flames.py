class special_symbol(Exception):
    def __init__(self,arg):
        self.msg=arg
player_1=input('player_1 name>')
player_2=input('player_2 name>')
name=player_1+player_2
for i in name:
    if i.split():
        if i.isalpha():
            pass
        else:
            raise special_symbol('special symbols or numbers are not allowed')

count=0
n=[]
for i in name:
    if i==' ':
        pass
    else:
        n.append(i)
print(n)
for i in range(len(n)):
    if n.count(n[i])>1:
        print('multi times',n.count(n[i]),'letter',n[i])
        print(n)
    else:
        count+=1
        print('single letter added is',n[i])
        print('total count is {}'.format(count))
print('count:',count)
result=['friends','love','affection','marriage','enemy','siblings']
print(result)
while len(result)>1:
    split_index=(count%len(result)-1)
    if split_index>=0:
        right=result[split_index+1:]
        left=result[:split_index]
        print('right index:',right)
        print('left index:',left)
        result=right+left
        print(result)
    else:
        result=result[:len(result)-1]
print('relationship status:',result[0])

