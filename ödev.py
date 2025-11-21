meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }
word = input("Anlamadığınız bir kelime yazın: ").upper()
if word in meme_dict.keys():
    a=meme_dict[word]
    print(a)
    
else:
    print("*"*30)
    print ("Bu kelime sözlükte yok doğru yazdığınızdan emin olun yada tekrar deneyin")
    print("*"*30)
