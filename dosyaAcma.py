dosya=open("dosya yolu","a",encoding="utf-8")

dosya.write("\nütopya ")
dosya.close()
print(dosya)



print(dosya.read(9))
print(dosya.readline())
print(dosya.readlines())
print(dosya.readline())
print(dosya.readline())
print(dosya.readline())


with open("dosya yolu","r",encoding="utf-8") as dosya:
print(dosya.read())
dosya.seek(5)
print(dosya.tell())
print(dosya.read(3))
