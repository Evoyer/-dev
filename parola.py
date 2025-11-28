import random
pslist=[]
while True:
    pd="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    lenp=int(input("Kaç karakterli bir şifre istiyosun\n:"))
    ps=""
    for i in range(lenp):
        kr=random.randint(0,len(pd))
        kp=pd[kr]
        ps=kp+ps
    print(f"Şifreniz:{ps}")
    pslist.append(ps)
    print(f"Şifreleriniz:\n{pslist}")
    dm=input("Bidaha kullanmak istermisin(e/h):").lower()
    if dm == "e":
        continue
    else:
        break
