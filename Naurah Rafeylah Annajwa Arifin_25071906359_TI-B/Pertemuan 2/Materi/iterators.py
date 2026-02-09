mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit)) #harus di panggil satu-satu ga bisa langsung muncul semua

#kenapa tetap bisa di print padahal dia error, interpretor?

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#bisa dipersingkat dengan menggunakan for
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)
