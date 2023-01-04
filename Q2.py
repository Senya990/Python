text = input("Введите текст: ")
words = input("Введите слова для замены через пробел так, как они написаны в тексте: ").split()
for word in words:
    text = text.replace(word, word.upper())
print(text)