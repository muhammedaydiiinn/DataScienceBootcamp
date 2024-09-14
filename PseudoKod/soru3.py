from math import sqrt

sayi = int(input("Bir sayı giriniz: "))
if sayi<2:
    print("Sayı asal değildir.")

asal = True
i = 2

while i<= sqrt(sayi):
    if sayi % i == 0:
        print("Sayı asal değildir.")
        asal = False
        break
    i += 1

if asal:
    print("Sayı asaldır.")