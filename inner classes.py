class person:
    def __init__(self):
        self.name='ps'
        self.db=self.Dob()
    def display(self):
            print('name:',self.name)
    class Dob:
            def __init__(self):
                self.dd=29
                self.mm=12
                self.yy=1998
            def display(self):
                    print('Dob={}/{}/{}'.format(self.dd,self.mm,self.yy))
e=person()
e.display()
person().db.display()