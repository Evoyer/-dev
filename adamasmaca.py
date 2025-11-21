import time
import random
wordlist1=["elma","armut","demir","kalem","çilek","ikilem","ahmet kaya","papatya","altın","elmas","paratoner","mermer","inek","kebap","dönme dolap","barış manço","aziz sancar","kurban bayramı","ballondor","televizyon","pagani","tesla"]
isim=input("İsmin nedir:").capitalize()
print("Adam asmacaya hoşgeldin "+isim)
time.sleep(2)
while True:
    can=10
    tlist=[]
    ylist=[]
    print("Hazırsan başlıyoruz")
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    print(0)
    time.sleep(1)
    word = random.choice(wordlist1)
    if word=="tesla":
        print("Bu hem araba markası hemde mucit ismi")
    if word=="pagani":
        print("Bu bir spor araba markası")
    if word=="ibiza:":
        print("Bu hem İspanyada bir şehir hemde bir araba markası")
    if word=="televizyon":
        print("Bu elektironik bir cihaz")
    if word=="ballondor":
        print("Bu futbolda verilen bir ödüldür")
    if word=="kurban bayramı":
        print("Bu bir dindeki bir bayramdır")
    if word=="aziz sancar":
        print("Bu kişi Türkiye için çok önemli bir bilim insanı")
    if word=="barış manço":
        print("Bu bir şarkıcı")
    if word=="elma":
        print("Bu bir meyve")
    if word=="armut":
        print("Bu bir meyve")
    if word=="demir":
        print("Bu bir maden")
    if word=="kalem":
        print("Bu genellikle okulda kullanılır")
    if word == "çilek":
        print("Bu bir yaz meyvesi")
    if word=="ikilem":
        print("Bu iki arada bir derede kalmak demek")
    if word=="ahmet katya":
        print("Bu bir şarkıcı ve iki ismi var")
    if word=="papatya":
        print("Bu bir çiçek ve çayı yapılır")
    if word=="altın":
        print ("Bu değerli bir maden")
    if word=="elmas":
        print("Bu değerli bir maden")
    if word=="paratoner":
        print("Yağmurda bizi koruyan bir eşya")
    if word=="mermer":
        print("Bu inşaatlarda kullanılan bir maddde")
    if word=="inek":
        print("Bu bir dinde tapılan bir şey")
    if word=="kebap":
        print("Bu Türkiye'nin en ünlü yemeğidir")
    if word=="dönme dolap":
        print("Lunaparktaki bir oyuncaktır ")
    print("Bu kelimenin uzunluğu:",(len(word)))
    while True:
        yt=input("Tahminin eğer kelimeyse'k'ye bas eğer harf ise'h'ye bas.Eğer kelime tahmini yapıp yanlış bilirsen"\
        "2 canın gider.Harf tahmini yaparsan ve yanlış olursada 1 canın gider:").lower() 
        if yt == "k":
            wordtahmin=input("Tahminini gir:").lower()
            if wordtahmin == word:
                print("Tebrikler "+isim+" tahminin doğru")
                break
            if wordtahmin!=word:
                print("Tahminin yanlış bir daha dene")
                can-=2
                ylist.append(wordtahmin)
        if yt =="h":
            harftahmin=input("Tahminini gir(küçük harflerle gir):").lower()
            if harftahmin in word:
                print("Tebrikler "+isim+" tahminin kelimenin içinde var")
                tlist.append(harftahmin)
            if harftahmin not in word:
                print("Tahminin yanlış")
                can-=1
                ylist.append(harftahmin)
            time.sleep(2)
        print("-"*30)
        print(f"Doğru tahminlerin:",str(tlist))
        print(f"Yanlış tahminlerin:",str(ylist))
        print("Kalan canın:",can)
        print("-"*30)
        time.sleep(2)
        if can<=0:
            print("Cevap buydu:",word)
            time.sleep(1)
            print("Canın bitti ölmene son")
            time.sleep(1)
            print(3)
            time.sleep(1)
            print(2)
            time.sleep(1)
            print(1)
            time.sleep(1)
            print(0)
            time.sleep(1)
            print("Asıldın ve öldün")
            time.sleep(2)
            break
    donme=input("Bi daha oynamak istermisin(e/h):").lower()
    if donme=="e":
        continue
    if donme=="h":
        break
