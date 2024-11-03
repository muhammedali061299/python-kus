def anamenu():

    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║  REHBER UYGULAMASI  ║")
    print("║                     ║")
    print("║  1-Kişi ekle        ║")
    print("║  2-Listele          ║")
    print("║  3-Ara              ║")
    print("║  4-Düzelt           ║")
    print("║  5-Sil              ║")
    print("║                     ║")
    print("║  Seçimiz nedir?     ║")
    print("╚═════════════════════╝")
    secim=input()
    if secim=="1":rehber_ekle(); anamenu()
    if secim=="2":rehber_listele(); anamenu()
    # if secim=="3":rehber_ara(); anamenu()
    # if secim=="4":rehber_düzelt(); anamenu()
    # if secim=="5":rehber_sil(); anamenu()




anamenu()

def rehber_ekle():
        dosya=open("rehber.txt","a")
        print("\n\n Rehbere eklenecek bilgileri giriniz")
        ad=input("Ad:")
        tel=input("Tel:")
        dosya.write(f"{ad}#{tel}\n")
        dosya.close()
        print("\n\nRehberdekiler(yeni şekli)")
        rehber_listele()
def rehber_listele():
        print("\n\nRehberiniz:")
        dosya=open("rehber.txt")
        okunan=dosya.readlines()
        #print(okunan)
        # a for a in okunan:
        for sıra,a in enumerate(okunan):
            b = a.split("#")
            #print(b{0},"\tTelefonu:",b{1})
            #print(sıra+1)"-"b{0},\tTelefonu",b[1])
            print(f"{sıra+1}-{b[0]},\t Telefonu:{b[1]}")
        dosya.close

def rehber_sil():
    print("Mevcut kayıtlar")
    rehber_listele()
    silinecek=input("Hangi kayıt silinecek(numarasını girin)")
    dosya=open("rehber.txt")
    okunan=dosya.readlines()
    dosya.close
    dosya.open("rehber.txt","w")

    for sıra,a in enumerate(okunan):
        if sıra != silinecek:dosya.write(a)  
def rehber_düzelt():
            pass



         