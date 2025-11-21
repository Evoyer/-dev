import time
import os
from random import shuffle
isim=input("İsmin nedir: ")
print("Merhaba "+isim)
print("Akılda tutma oyununa hoş geldin")
xp=0
while True:
    seviye=int(input("hangi seviyeden başlamak istersin(1/2/3/4/5): "))
    if seviye == 1:
        liste1=[1,2,3]
        shuffle (liste1)
        print(liste1)
        time.sleep(2)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print(0)
        time.sleep(0.5)
        print("Hazır")
        time.sleep(0.5)
        print("Başla")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        tahmin=input("Hadi bakalım kolay gelsin :) : ")
        tahmin=[int(i) for i in tahmin.split()]
        if tahmin==liste1:
            print("Tebrikler "+isim)
            xp+=2
            print("Seviyen:",xp)
        else:
            tahmin1=input("Bidaha dene: ")
            tahmin1=[int(ı) for ı in tahmin1.split()]
            if tahmin1 == liste1:
                print("Bu sefer başardın tebrikler "+isim)
                xp+=1
                print("Seviyen:",xp)
            else:
                print("Üzgünüm bir dahaki sefere")
                print("Cevap buydu:",liste1)
                xp-=1
                print("Seviyen:",xp)
    if seviye == 3:
        liste2 = [1,2,3,4,5]
        shuffle(liste2)
        print(liste2)
        time.sleep(2)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print(0)
        time.sleep(0.5)
        print("Hazır")
        time.sleep(0.5)
        print("Başla")
        time.sleep(1)
        os.system('cls' if os.name=='nt' else 'clear')
        tahmin=input("Hadi bakalım kolay gelsin:) : ")
        tahmin=[int(i) for i in tahmin.split()]
        if tahmin==liste2:
            print("Tebrikler "+isim)
            xp+=6
        else:
            tahmin1=input("Bir daha dene: ")
            tahmin1=[int(ı) for ı in tahmin1.split()]
            if tahmin1==liste2:
                print("Bu sefer başardın "+isim)
                xp+=3
            else:
                print("Üzgünüm bir dahaki sefere")
                print("Cevap buydu:",liste2)
                xp-=2
        print("Seviyen:",xp)
    if seviye==2:
        liste3=["tüfek","dünya","güven"]
        shuffle(liste3)
        print(liste3)
        time.sleep(2)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print(0)
        time.sleep(0.5)
        print("Hazır")
        time.sleep(0.5)
        print("Başla")
        time.sleep(1)
        os.system('cls' if os.name=='nt' else 'clear')
        tahmin=input("Hadi bakalım kolay gelsin:) : ")
        tahmin=tahmin.split()
        if tahmin==liste3:
            print("Tebrikler "+isim)
            xp+=4
        else:
            tahmin1=input("Bir daha dene: ")
            tahmin1=tahmin1.split()
            if tahmin1==liste3:
                print("Bu sefer başardın tebrikler "+isim)
                xp+=2
            else:
                print("Üzgünüm bir dahaki sefere")
                print("Cevap buydu:",liste3)
                xp-=3
        print("Seviyen:",xp)
    if seviye == 4:
        liste4 = ["elma","armut","kavun","karpuz","üzüm"]
        shuffle(liste4)
        print(liste4)
        time.sleep(2)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print(0)
        time.sleep(0.5)
        print("Hazır")
        time.sleep(0.5)
        print("Başla")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        tahmin=input("Hadi bakalım kolay gelsin :) : ")
        tahmin=tahmin.split()
        if tahmin == liste4:
            print("Tebrikler "+isim)
            xp+=8
        else:
            tahmin1=input("Birdaha dene: ")
            tahmin1=tahmin1.split()
            if tahmin1==liste4:
                print("Bu sefer başardın tebrikler "+isim)
                xp+=4
            else:
                print("Üzgünüm bir dahaki sefere")
                print("Cevap buydu:",liste4)
                xp-=4
        print("Seviyen:",xp)
    if seviye==5:
        liste5=[1,2,3,4,5,6,7,8,9,10]
        shuffle(liste5)
        print(liste5)
        time.sleep(10)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print(0)
        time.sleep(0.5)
        print("Hazır")
        time.sleep(0.5)
        print("Başla")
        time.sleep(1)
        os.system("cls" if os.name=="nt" else "clear")
        tahmin=input("Hadi bakalım kolay gelsin:) : ")
        tahmin=[int(i) for i in tahmin.split()]
        if tahmin==liste5:
            print("Tebrikler "+isim)
            xp+=10
        else:
            tahmin1=input("Bi daha dene: ")
            if tahmin1==liste5:
                print("Tebrikler bu sefer başardın "+isim)
                xp+=5
            else:
                print("Üzgünüm bir dahaki sefere")
                print("Cevap buydu:",liste5)
                xp-=5
        print("Seviyen:",xp)   
    dönme=input("Bi daha oynamak istermisin(e/h): ")
    if dönme.lower()=="e":
        continue
    if dönme.lower()=="h":
        break
    
