'''3.Dastur foydalanuvchidan “O‘zbekiston poytaxti nima?” deb so‘raydi. “Toshkent” deb to‘g‘ri javob berguncha so‘rashda davom etadi.'''



poytaxt = "Samarqand"

while True :
    x = input("O'zbekiston poytaxti nima? ")
    
    if x.capitalize() == poytaxt :
        print(f"Siz to'g'ri topdingiz")
        break
    else :
        print("Poytaxtni noto'g'ri kiritdingiz")