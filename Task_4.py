my_list=[1, 2, 4, 5, 63, 13, 32, 10, 54, 78]
print("List:",my_list)
min_list=my_list.index(min(my_list))
max_list=my_list.index(max(my_list))
print("Eng kichik qiymat indeksi:",min_list)
print("Eng katta qiymat indeksi:",max_list)
my_list.insert(min_list+1, 0)
my_list.insert(max_list+2, 0)
print("Yakuniy natija:", my_list)