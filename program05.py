'''5.1 donasi 2500 so‘m bo‘lgan mahsulotdan foydalanuvchi 1 tadan 10 tagacha olganida umumiy narxlarni jadval ko‘rinishida chiqaring.'''



number = int(input("Sonni kiriting: "))

if number > 0:
    for i in range(1,number+1):
        i *= 2500
        print(f"{number} dona = {i}")
else:
    print("Buday narx yo'q" )