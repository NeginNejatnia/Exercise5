import cmath 
a = float(input("Enter a :"))
b = float(input("Enter b :"))
c = float(input("Enter c :"))

d = ((b**2)-(4*a*c))

ans1 = (-b-cmath.sqrt(d))/(2*a)
ans2 = (-b+cmath.sqrt(d))/(2*a)
#print('Result :'.format(ans1,ans2))
print('Result is {0} and {1}'.format(ans1,ans2))   
