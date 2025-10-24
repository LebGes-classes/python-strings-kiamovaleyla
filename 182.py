text = input('Введите текст из слов на английском языке: ')

list_of_words = []
word = ""

for char in text:
    if char.isalpha():
        word += char
    else:  # если символ не буква (пробел, запятая, точка)
        if word:
            list_of_words.append(word)
            word = ""
        # небуквенные символы не добавляем в список слов

# Добавляем последнее слово, если текст заканчивается буквой
if word:
    list_of_words.append(word)


K = 0
for word in list_of_words:
    if len(word) > K:
        K = len(word)


low_alph = 'abcdefghijklmnopqrstuvwxyz'
high_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'



encrypted_text = ""
for char in text:
    if char in high_alph:  # шифруем большие буквы
        encrypted_text += high_alph[(high_alph.index(char) + K) % 26]
    elif char in low_alph:  # шифруем буквы нижнего регистра
        encrypted_text += low_alph[(low_alph.index(char) + K) % 26]
    else:  # остальные символы без изменений
        encrypted_text += char


print(encrypted_text)
print(K)