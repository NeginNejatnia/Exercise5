name = input()
small = 0
capital = 0
for i in name:
    # check kardan horof kochik va bozorg
    if i.islower():
        small += 1
    elif i.isupper():
        capital += 1
if capital > small:
    # neveshtane tamami kalame ba horof bozorg ya kochak
    print(name.upper())
else:
    print(name.lower())