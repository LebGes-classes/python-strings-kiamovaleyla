text = input("Введите текст: ")

words = []
word = ""
for char in text:
    if char == " ":
        if word:
            words.append(word)
            word = ""
    else:
        word += char
if word:
    words.append(word)

# Собираем слова в обратном порядке
mirrored_text = ""
for i in range(len(words)-1, -1, -1):
    if mirrored_text:
        mirrored_text += " "
    mirrored_text += words[i]

# Перевернутая строка
reversed_text = ""
for i in range(len(text)-1, -1, -1):
    reversed_text += text[i]

print(f"Исходная: «{text}»")
print(f"Зеркальные слова: «{mirrored_text}»")
print(f"Перевернутая: «{reversed_text}»")