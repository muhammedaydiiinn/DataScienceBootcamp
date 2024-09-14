dizi = input("Bir dizi girin: ").split(" ")

n = len(dizi)

tekrarVar = False

i = 0

while i < n:
    j = i + 1

    while j < n:
        if dizi[i] == dizi[j]:
            tekrarVar = True
            break
        j += 1

    if tekrarVar:
        break

    i += 1

if tekrarVar:
    print("Dizide tekrar eden eleman var")
else:
    print("Dizide tekrar eden eleman yok")