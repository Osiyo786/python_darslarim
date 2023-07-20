name=input("Ismingizni kiriting:")
age=int(input("Yoshingizni kiriting:"))
place=input("Tug'ilgan joyingizni kiriting:")
text="Mening ismim %s, yoshim %d da, %sda tug'ilganman." % (name, age, place)
text2=f"Mening ismim {name}, yoshim {age} da, {place}da tug'ilganman."
text3="Mening ismim{}, yoshim {} da, {}da tug'ilganman".format(name, age, place)
print(text)
print(text2)
print(text3)

