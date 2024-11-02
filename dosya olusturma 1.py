#open(f"rehber.txt","w")
#open(f"rehber.txt","w"write("Buse eroğlu")
a=open(f"rehber.txt","w")
a.write("Buse eroğlu,:")

#a =open(f"rehber.txt","w")
## w=write modunda öncekiler silinir.
a=open(f"rehber.txt","a")
#a =append ile açıldığında öncekilere eklenir.
for b in range(10):
    #a.write(str(b))
    a.write(f"{str(b)}\n")

#a =open(f"rehber1.txt","w") r=read (eğer mod belirtilmezse yine r kabul edilir.)
#a =open(f"rehber1.txt","w" , encoding=utf8 #türkçe karakter desteği için utf8
#a.write("Çarşamba")

#a = open(f"rehber.txt","r")# r=read
#a = open(f"rehbercagir.py) # eğer mod belirtilmez ise r olarak kabul edilir.
a=open(f"dosya_3_okuma1.py",encoding="utf8") #türkçe karakter
print(a)
okunan=a.read()
print(okunan)



