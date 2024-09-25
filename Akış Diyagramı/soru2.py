import math
x = int(input("Sayı Giriniz: "))
asalMi = False
if x == 1:
    asalMi = False
elif x == 2:
    asalMi = True
else:
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            asalMi = False
            break
        else:
            asalMi = True
if asalMi:
    print("Asal")
else:
    print("Asal Değil")