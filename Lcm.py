a = int(input('Enter your number a : '))
b = int(input('Enter your number b : '))

def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b
    while(True):
        if((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

lcm(a,b)
print("LCM = ", lcm(a, b))