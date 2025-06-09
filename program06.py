'''6.Kompyuter bir son o'ylaydi (masalan, 5). Foydalanuvchi maksimal 3 marta topishga harakat qiladi. To‘g‘ri topsa: “Topdingiz!”, aksi holda: “Urinishlar tugadi.”'''



from random import randint

number = randint(-999,999)
print(number)

counter = 0

while counter < 3 :
    x = int(input("Sonni kirit: "))
    counter += 1

    if x == number :
        print("To'g'ri topdingiz!")
        break
    else:
        print("Yana davom et.")

else :
    print("Urunishlar tugadi.")