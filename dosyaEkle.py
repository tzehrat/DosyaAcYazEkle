#     ****SAYFAYA ELEMAN EKLEME *****

with open("C:/Users/beyra/desktop/yenisoya.txt","r+",encoding="utf-8") as dosya:
        dosya.write("aloha!\n")


#*********SAYFA SONUNA ELEMAN EKLEME*******

with open("C:/Users/beyra/desktop/yenisoya.txt","a",encoding="utf-8") as dosya:
   dosya.write("\naloha!")


#***********SATFA BALINA ELEMAN EKLEME***********
with open("C:/Users/beyra/desktop/yenisoya.txt", "r+", encoding="utf-8") as dosya:
  dosya.seek(0)
  dosya.write("hhgjgjgj")



# *********SAYFA ORTASINA ELEMAN EKLEMEME********



with open("C:/Users/beyra/desktop/yenisoya.txt", "r+", encoding="utf-8") as dosya:
    liste=dosya.readlines()
    liste.insert(3,"ohhbe\n")
    dosya.seek(4)
    for i in liste:
        dosya.write(i) ya da
    dosya.writelines(liste)

