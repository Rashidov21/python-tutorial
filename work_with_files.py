from faker import Faker

fake = Faker() # fake ma'lumotlarni hosil qilish obyekti
# open() - fayllar bilan ishlash vaularni ochish uchun funksiya
# f = open("./test.txt",mode='r', encoding='utf-8')
# r - read , o'qish
# r+ - read + write , o'qish va yozish
# w - write , yozish
# w+ - read + write , o'qish va yozish
# a - append ,write , yozish
# a+  - read + write , o'qish va yozish
# x - faylni hosil qilish rejimi (agar fayl oldindan mavjud bo'lsa xatolik vujudga keladi : FileEx istsError;)
# x+ - faylni hosil qilish  o'qish va yozish rejimi (agar fayl oldindan mavjud bo'lsa xatolik vujudga keladi : FileExistsError;)
# b - binary , binar rejim fayl metodlari bytes ma'lumot turini qaytaradi
# print(f) # <_io.TextIOWrapper name='./test.txt' mode='r' encoding='utf-8'>
# print(dir(f))

# print(f.read()) # faylni o'qish
# f.close() # faylni yopadi

# f = open("./test.txt",mode='a+', encoding='utf-8')
# for i in range(10):
#     fake_name = fake.name()
#     f.write(f"{fake_name}\n")
    
# f.close()

# f.writelines()

# with open('./test.txt', 'r+', encoding='utf-8') as file:
    # file.writelines("asslomu alaykum")
    # print(file.read())
    # print(file.writable()) # True
    
# with open('./test.txt', 'r+', encoding='utf-8') as file:
    # file.writelines("asslomu alaykum")
    # print(file.read())
    # print(file.readline())
    # print(file.readline()) # faqat bittadan qatorni o'qish
    # print(file.writable()) # False
    # print(file.readlines()) # hamma qatorlarni o'qish va massivga holatida qaytarish
    # print(file.truncate(7))
    # file.buffer.write(bytes("Python", "utf-8"))