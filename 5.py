m1="Şehirler"
m2="Ankara"
m3="İzmir"
m4=f"iller{m3} -- {m2}"
m5=f"{m1}={m4} {m2}"
print (m4)
print(m5)



#pythonda string formatlama (metin şekillendirme işlemi)
print(f"(Şehirler: {m2}, {m3}")
print("Şehirler {},{}.format(m2,m3)")
print("Şehirler %s,%s %(m2,m3)")


     


meyveler=["Elma","Muz","Nar","Dut"]
çorbalar=["Tarhana","Mercimek","Yayla"]

print(meyveler)
print(*meyveler)
print(*meyveler,sep=",")
print(*meyveler,sep="n")

print("Van","Muş","Çan","Bor")
print("Van","Muş","Çan","Bor", sep="")
print("Van","Muş","Çan","Bor", sep="-")

print("Van","Muş","Çan","Bor",end="")
print("Van","Muş","Çan","Bor",sep="-",end="")
print("şehirler")

#end parametresi print ile yazdıktan sonra ne yapılacağını belirtir.
#sep seperate parametresi print ile birden çok ifade arasında nelerin olacağını ifade eder
