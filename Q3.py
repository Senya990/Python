text = input("Введите текст: ")
kolvo = sum(text.count(x) for x in '.?!')
print(f"Кол-во предложений = {kolvo}")