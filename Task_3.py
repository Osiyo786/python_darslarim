url = input("Urlni kiriting:")
if url.find(" ") != -1:
    print("Ushbu urldagi bo'sh probellarni %20 belgisiga o'zgartirish kerak!")
    url = url.replace(" ", "%20")
else:
    print("Ushbu urlda xatolik mavjud emas!")
print("Url:", url)
