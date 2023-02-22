# task 1
# 10 bilan 35 orasida tasodifiy 5 ta sodan iborat massiv hosil qiling

# task 2
# task 1 taskni list generator orqali qiling


# task 3
# massivda turli turdagi elementlar bor massivni saralab barcha elementlarni turi boyicha saralab yozing

# arr = [True, 1,1.3,3.3,"str", "qale"]
# bools = [True]
# ints =  [1]
# floats = [1.3,3.3] 
# strs = ["str", "qale"]

# task 4
# faker orqali 30 ta user ismini oling ismda "a" harfi 2 marta ishtirok etganlarini alohida 
# dict qilib yozing kalit sifatida ismni o'zini qiymat sifatida random son ishlating

# task 5 
# user telefon raqam kiritadi uni togri yoki notogri kiritganini aniqlovchi dastur tuzing
# +99 (893) 333-33-33


# task 6
# while orqali userdan kamida 5 ta sana qabul qiling
# agar sana haqiqatda to'g'ri sana bo'lsa uni massivga yozing aks holda davom eting
# d = "12.36.2012" >> False
# d = "12.30.2012" >> True

# task 7
#  Odil har kuni muntazam 9 soatdan uxlashni reja qilgan. Siz uning uchun u soat nechida uxlashga
#  yotsa roppa rosa 9 soatdan keyin soat nechi bo’lishini hisoblaydigan dastur yozishingiz kerak.
#  Agar Tohir soat 22:00 da uhlashga yotsa demak uyg’onganida soat 07:00 bo’lishini ko’rsatishingiz kerak.
# Kirish : ‘22:00’
# Chiqish : ‘07:00’

# task 7 

# 12 ta ishchi ism familyasini Faker orqali hosil qiling
# har bir ishchi 12 oy davomida (1 yil) har bir oyda ma'lum bir miqdorda oylik maosh olgan
# oylik maoshlar stabil oylik maosh summasidan ishchini ishlashiga qarab ayrim oylarda +5% ko'proq , ayrim oylarda -5% kamroq bo'lishi mumkin. Siz ushbu malumotlardan foydalanib hisoblashingiz kerak. 
# 1-Har bir ishchini 12 oyda olgan umumiy ish haqi summasi 
# 2- Har bir ishchini kvartallar boyicha ish haqlarini 
# 3- yil davomida eng ko'p maosh olgan ishchini 
# 4- yil davomida eng kam moash olgan ishchini 
# 5- eng kop maosh olgan ishchini eng kam olgan  bilan oyliklari o'rtasidagi farqni 

# task 8 
# Istalgancha sonlarni qabul qilib ularni yigindisini qaytaruvchi function yozing 
# sonlar butun yoki qoldiqli bo'lishi mumkin , lekin natija butun son bo'ladi


# task 19 

# Dasturga changi sportchilarini natijalari ketma ket kelib tushadi 
# dastur ularni tekshirib eng yaxshilarini royhat boshiga yomonlarini pastga qarab qo'shib  #kelishi kerak , natijalar , sarflagan vaqti sekunlarda va bosib otgan masofasi km da 
# kam vaqt sarflab kop km bosgan sportchilar birinchiga chiqariladi
# input : 'John' , 4.5 , '3:30'
p = [
    ('John' , 4.9 , '3:10'), # 1
    ('Mike' , 4.1 , '3:27'), # 3
    ('David' , 4.7 , '3:30'), # 2
]

p.sort(key=lambda x : x[1], reverse=True)

for player in p:
    p.sort(key=lambda x:int(player[2].split(":")[0]))
    p.sort(key=lambda x:int(player[2].split(":")[1]))
    
print(p)

# task 20
# Sinfda imtihondan song oquvchilarni qayta partalarga joylashtirish 
# bo'lyapti, sinf rahbari qizlardan imtihon natijasiga kora eng yuqorilarini bollardan eng pastlari bilan birga joylashtirmoqchi , dastur vazifasi oquvchilar natijalarini saralab qizlarni eng yaxshi natijalilarini bollarni eng yomonlari bilan bitta ro'yhatga keltirish 

# input : "John" ,"male", 99 
# output : [("famale", "Sara", 89), ("male", "John", 36)]