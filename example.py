def Notları_gir():
    ad=input("ad gir:")
    soyad=input("soyad gir:")
    not1=int(input("not 1 gir:"))
    not2=int(input("not 2 gir:"))
    not3=int(input("not 3 gir:"))
    with open("sınavdosyası.txt","a",encoding="utf-8") as dosya:
        dosya.write(ad+" "+soyad+":"+not1+","+not2+","+not3)


def Ortalamaları_oku():
        with open("sınavdosyası.txt", "a", encoding="utf-8") as dosya:
            ortalama=(not1+not2+not3)/3
            return ad+" "+soyad+":" + ortalama

while True:
    islem=input("1-Notlari gir\n2-ortalamaları oku\n3-çıkış ")
    if islem=="1":
        print(Notları_gir())
    elif islem=="2":
        print(Ortalamaları_oku())
    else:
        break
