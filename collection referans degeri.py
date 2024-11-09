a = [2,4,1,6]  #a adresi atatürk mah.cumhuriyet cd. no 2
b = [3,2,5,1]
c = a  # collectionlarda referans değer atanır.      #c adresi atatürk mah.cumhuriyet cd. no 2
d = c[:] # collection içindeki değerler d referans atanır.

print ("a: ",a)
print ("b: ",b)
print ("c: ",c)
print ("d: ",d)

a[2] = "h"
print ('\nc[1] = "h" sonrası')
print ("a: ",a)
print ("b: ",b)
print ("c: ",c)
print ("d: ",d)
# devamı sonraki sütunda..
