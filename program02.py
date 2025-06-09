'''2.1 dan 5 gacha bo‘lgan sonlar va ularning kvadratlarini ekranga chiqaring. Misol: 1^2 = 1, 2^2 = 4, ...'''



number = int(input("Sonni kiriting: "))

for i in range(1,number+1):
    num = pow(i,2)
    print(f"{i} ^ 2 = {num}")