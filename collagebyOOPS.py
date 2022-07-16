class collage:
    print('VNR VJIET')
    def __init__(self,rnum,name,branch):
        self.rnum=rnum
        self.name=name
        self.branch=branch
        self.sub=subjects()
    def admission(self):
        print('your name:{} \nyour roll number:{} \nyour branch:{}'.format(self.name,self.rnum,self.branch))
class inclass(collage):
    def __init__(self,rnum,name,branch,grade,section):
        super().__init__(rnum,name,branch)
        super().admission()
        self.grade=grade
        if grade=='A':
            print('GRADE A well performance')
        elif grade=='B':
            print('''GRADE B
    >>betterluck next time''')
        self.section=section
        if self.section=="a" or self.section=="A":
                print('your alloted to first section A')
        elif self.section=='b' or self.section=='B':
                print('your alloted to second section B')
class subjects():
    def jr(self):
        print('EIE branch')
        print('subjects')
        self.m1=print('m1(maths)')
        self.LDIC=print('linear intigrated circuits')
        self.language=print('''ENGLISH
                    for communication skills''')
y=inclass('16071A1010','PS','EIE','B','A')
y.sub.jr()

