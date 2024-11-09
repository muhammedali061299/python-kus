import re
metin1 = "Bugün hava çok soğuk"
metin2 = "Bursa çok sıcak"
metin3 = "Bugün hava soğuk."

#aranan="^Bu."soğuk$" # başında bu olan ve soğuk ile biten
#aranan ="^Bug*" # başında bug olanları ara
aranan= "o.*"# o ile başlayan ifadeler.

print(re.search(aranan, metin1))
print(re.search(aranan, metin2))
print(re.search(aranan, metin3))
# foldercode.com\xu55
deger=re.search(aranan,metin1)
print(type(deger))



import re
xxx = "Ahmet al renkli bir şal aldı."

# tüm al ifadelerinin listesi
print(re.findall("al", xxx))

# şal ifadesini ara
print(re.search("şal", xxx))

# “al” a göre böl
print(re.split("al", xxx)) 

# Boşlukları zzz yap
print(re.sub(" ", "zzz", xxx)) 



import re
xxx="Elma,Armut,Muz"

#"al a göre böl"
print(re.split(",",xxx))
