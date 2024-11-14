import random

secenekler = ["Tas", "Kagit", "Makas"]

while True:
    random_bot = random.choice(secenekler)
    secilen = input("Tas kagit makas!\n")

    if secilen == "Tas":
        if random_bot == "Tas":
            print("Rakibiniz de taş yaptı, berabere!")
        if random_bot == "Kagit":
            print("Rakibiniz kağıt yaptı, kaybettiniz!")
        if random_bot == "Makas":
            print("Rakibiniz makas yaptı, kazandınız!")
    elif secilen == "Kagit":
        if random_bot == "Tas":
            print("Rakibiniz de taş yaptı, kazandınız!")
        if random_bot == "Kagit":
            print("Rakibiniz kağıt yaptı, berabere!")
        if random_bot == "Makas":
            print("Rakibiniz makas yaptı, kaybettiniz!")
    elif secilen == "Makas":
        if random_bot == "Tas":
            print("Rakibiniz de taş yaptı, kaybettiniz!")
        if random_bot == "Kagit":
            print("Rakibiniz kağıt yaptı, kazandınız!")
        if random_bot == "Makas":
            print("Rakibiniz makas yaptı, berabere!")
    else:
        print("Nolur gösterilen üç seçenekten birini gösterildiği gibi gir!")
        continue
    
    res = input("Tekrar oynamak ister misin?(y/n)")
    if res == "y":
        continue
    elif res == "n":
        break
    else:
        print("Yanlış değer girdin kapatıyoz dükkanı")
        break
