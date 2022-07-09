# f=open('name.txt','w')
# f.writelines(['ps\n','pop\n','pip\n'])
# f.close()
# x=open('body.txt','w')
# x.write('iam happy here and\n i wish the same from you')
# x.close()
# #
with open('name.txt','r') as namef:
    with open('body.txt','r') as bodyf:
        body=bodyf.read()
        for name in namef:
            mail='hello'+'___ '+name.strip()+'\n'+body
            print(mail)
            print()
