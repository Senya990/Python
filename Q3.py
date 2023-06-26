text = input("Введите текст не забывая знаки препинания: ")
kolvo = sum(text.count(x) for x in '.?!')
print(f"Кол-во предложений = {kolvo}")
