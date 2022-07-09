employ ={'1:name':{'f.name=':input('firstname='),'l.name=':input('lastname=')},
         '2:department':['''for 'degital','marketing','sales' only'''],
         '3:experence':int(input('experence=')),
         '4:salary=':'based on experence'}
if employ['3:experence']> int(2):                  #int() not working ,direct 2 is not working
  print('expected good salary')

else:print('better luck nextime')

print(employ['2:department'])









