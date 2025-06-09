'''4.Kompyuter 3 xonali maxfiy raqam tanlaydi (masalan, 725). Foydalanuvchi to‘g‘ri topmaguncha kiritishda davom etadi. Har gal noto‘g‘ri kiritsa: “Yana urinib ko‘ring” deb yozilsin.'''



from random import randint

number = randint(-999,999)
print(number)

while True :
    num = int(input("Sonni kiriting: "))
    if num == number :
        print("Siz to'g'ri topdingiz")
        break
    else :
        print("Yana urunib ko'ring")