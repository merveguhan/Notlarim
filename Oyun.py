#Oyun

import random

def bsyr_secimi_uret():
    n=random.randint(1,3)
    if n ==1:
        return "tas"
    elif n==2:
        return "kagit"
    else:
        return "makas"
    

while True:
    kullanici_secimi =input(   "tas? kagit? makas?" )
    bsyr_secimi = bsyr_secimi_uret()
    print("Bilgisayar: ", bsyr_secimi)

    if bsyr_secimi == kullanici_secimi:
        print ("Berabere")
    elif bsyr_secimi == "tas" and kullanici_secimi == "kagit":
        print("Siz kazandiniz")
    elif bsyr_secimi == "kagit" and kullanici_secimi == "makas":
        print("Siz kazandiniz")
    elif bsyr_secimi == "makas" and kullanici_secimi == "tas":
        print("Siz kazandiniz")
    else:
        print("Kaybettiniz")
    