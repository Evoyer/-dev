import random
import time
pslist={}
parola="345123"
print("*"*40)
print(f"Uygulama parolanız:{parola}\n!!!UYARI LÜTFEN UNUTMAYIN")
print("*"*40)
while True:
    mod=int(input("1-Şifre ekleme\n2-Şifreleri görme\n3-Şifre silme\n:"))
    if mod==1:
        pd="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        lenp=int(input("Kaç karakterli bir şifre istiyosun\n:"))
        pr=input("Bu şifre hangi program için\n:").capitalize()
        ps=""
        for i in range(lenp):
            kr=random.randint(0,len(pd)-1)
            kp=pd[kr]
            ps=kp+ps
        print(f"Şifreniz:{ps}")
        pslist.update({pr:ps})
    if mod == 2:
        hak=3
        while hak>0:
                pasw=input("Lütfen şifrenizi giriniz\n:")
                if pasw==parola:
                    gr=input("Hangi şifreyi görmek istersiniz(Hepsi yazarsanız tüm şifreler)\n:").capitalize()
                    if gr in pslist.keys():
                        sn=pslist[gr]
                        print(f"{gr} adlı şifre:{sn}")
                        input("Devam etmek için ENTER a bas")
                    if gr=="Hepsi":
                        print(pslist.items())
                        input("Devam etmek için ENTER a bas")
                    break
                else:
                    hak-=1
    if mod == 3:
        gs=input("Hangi şifreyi silmek istiyosun\n:").capitalize()
        if gs in pslist.keys():
            sl=input(f"{gs} adlı şifre silinecek eminmisiniz(e/h):").lower()
            if sl == "e":
                pslist.pop(gs)
                print(f"{gs} adlı şifre siliniyor... ")
                time.sleep(2)
                print (f"{gs} adlı şifre silindi")
                time.sleep(1)
            else:
                continue
    dm=input("Bidaha kullanmak istermisin(e/h):").lower()
    if dm == "e":
        continue
    else:
        break
