# task 1 
# 1. Foydalanuvchidan soat nechi ekanini so’rang bu int son bo’ladi , agar qiymat 4 bilan 10 ni orasida bo’lsa print(‘Hayirli tong’)  agar 10 bilan 17 ni orasida bo’lsa print(‘Hayirli kun’) 17 bilan 23 ni orasida print(‘Hayirli kech’) cmd ga chiqadi.

# task 2 
# while orali foydalanuvchidan Ismini va Yoshini kiritishini so’raydigan va ismi nechta belgidan iborat bo’lsa uni yoshiga ko’paytiradgan dastur tuzing.

# task 3 
# Foydalanuvchi bergan sonlar oralig’idagi barcha toq sonlarni listga yozuvchi kod yozing: 
# masalan 5  bilan 10 orasidagi sonlar > nums = [6,7,8,9,10]

# task 4 
# Berilgan qatorda unlilar sonini topadigan dastur yozing topilishi kerak bo’lgan unlilar sifatida (a, i, u,e,o) harflari ko’rib chiqiladi. Kiruvchi matn kichkina harflardan tashkil topgan va probellar bilan ajratilgan bo’lishi mumkin.
# import time
# import requests # pip install requests
# from bs4 import BeautifulSoup as bs  #pip install bs4

# url = f"https://ismlar.com/category/Boshqalar"

# def connect_to_site(url,index):
#     res = requests.get(url+f"?page={index}")
#     if res.status_code == 200:
#         return res
#     else:
#         return False

# def write_data(data):
#     with open("names.txt", "a", encoding='utf-8') as file:
#         for line in data:
#             file.write(f"{line}, ")
            
# def parser(index):
#     obj_parse = connect_to_site(url,index)
#     print(obj_parse)
#     if obj_parse:
#         page = bs(obj_parse.text, "html.parser")
#         h1 = page.findAll("h1", class_="font-bold text-2xl text-cyan-500")
#         names = [x.text.strip() for x in h1]
#         print(names)
#         write_data(names)
#     else:   
#         time.sleep(1)
#         print("Error")        
#     return True

# for i in range(1,190):
#     done = parser(index=i)
#     print(done)
#     if done:
#         print(i)
        
        
        
        
# task 
# faker moduli orqali 15 ta davlat nomi ularga tasodify raqamlar biriktirilgan holatda ma'lumotlarni hosil qilib txt faylga yozing
# misol :
# 1	 Индия	    1 437 239 000	
# 2	 Китай[31]	1 411 778 724	
# 3	 США[37]	331 449 281	
# 4	 Индонезия	287 551 900	
# 5	 Пакистан	242 464 446	
# 6	 Нигерия	229 265 016	
# 7	 Бразилия	222 618 810	
# 8	 Бангладеш	177 445 977	
# 9	 Россия[44]	147 190 000	
# 10 Мексика	127 792 286	
# 11 Япония	    125 950 000	1967 
# 12 Эфиопия	124 079 000	
# 13 Филиппины	113 727 390	
# 14 Египет	    112 076 440	
# 15 ДРК	    101 780 263	

# task 
# stringda son berilgan  siz shuday kop xonali sonlarni xonalarini alohida alohida qilib oralarida bo'sh joylar bilan chiqaring
# input:"1437239000"
# output:1 437 239 000

# task 1
    # task 1.1
    # Berilgan matnda eng kop ishtirok etgan sozni toping 
    # task 1.2
    # Eng kop ishtirok etgan sozni 'baqlajon' so'ziga almashtiring
    
# text = """
# Dasturlashning mohiyati nimada?
# Dasturlash nima python uchun ishlatiladi u nimaga kerak?
# Kompyuter python bilan qanday muomila qilish python kerak ?
# Dasturlash uchun python nimalar kerak ?
# Dasturlash python atrofimizda.
# """
# text_arr = [t.replace("\n", " ").replace("?","").replace(" ", "") for t in text.split(" ")]
# print(text_arr)
# data = []
# for i,v in enumerate(text_arr):
#     temp = {
#         "text":v,
#         "index":i,
#         "count":text_arr.count(v)
#     }
#     data.append(temp)

# data.sort(key=lambda x:x["count"], reverse=True)
# print(data[0].get("text"))
# print(data[0].get("count"))


# data = []
# for t in text_arr:
#     data.append((t,text_arr.index(t)))

# for text_data in data:
#     for i in  range(len(data)-1):
#         # print(text_data[0])
#         # print(data[i][0])
#         if text_data[0] == data[i][0]: 
#             temp = list(text_data)
#             temp.append()
# print(data)