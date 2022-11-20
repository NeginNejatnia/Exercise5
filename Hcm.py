a = int(input('Enter your number a : '))
b = int(input('Enter your number b : '))

def Hcm(a, b):
    if(b == 0):
        return a
    else:
        return Hcm(b, a % b)

Hcm(a, b)
print("HCF = ", Hcm(a, b))