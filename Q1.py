str0 = input("Введите строку: ")
str1 = str0.lower()
str2 = str1.replace(" ", "")
str3 = str(str2[::-1])

if str2 == str3:
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")
