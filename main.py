a = int(input("kaç kelime araştıracaksın"))
for i in range(a):
    sozluk = {}
    sozluk["cringe"] = "Garip ya da utandırıcı bir şey"
    sozluk["lol"] ="Komik bir şeye verilen cevap"
    print(sozluk)
    ara = input("bir kelime ara")
    if ara == "cringe":
        print("cringe = Garip ya da utandırıcı bir şey" )
    elif ara =="lol":
        print("lol = Komik bir şeye verilen cevap")
    elif ara != "cringe" or "lol":
        print("sonuç yok")
