txt = input(' Enter your txt = ')
a1 = txt.find('h')
a2 = txt.find('e',a1+1)
a3 = txt.find('l',a2+1)
a4 = txt.find('l',a3+1)
a5 = txt.find('o',a4+1)

horof = a1>=0 and a2>a1 and a3>a2 and a4>a3 and a5>a4
if horof:
    print('YES')
else:
    print ('NO')