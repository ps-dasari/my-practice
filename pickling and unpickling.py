import pickle
class employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print(self.eno,'\t',self.ename,'\t',self.esal)
# with open('newp.dat','wb') as f:
#     e=employee(100,'ps',25000)
#     pickle.dump(e,f)
#     print('pickling done')
# with open('newp.dat','rb') as f:
#     obj=pickle.load(f)
#     print('unpickling done')
#     obj.display()




