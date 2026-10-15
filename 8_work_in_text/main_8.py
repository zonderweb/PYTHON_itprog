# Функції для роботи з текстом
word = list("itproger")
# word[0] = 'P'
# print(len(word))
word.append("!")
# print(word.count("g"))
result = ''.join(word)
print(word)
print(result)
print(result.lower())  # в нижній регістр
print(result.upper())  # в верхній регістр
print(result.capitalize())  # перша літера велика
print(result.isupper())  # перевірка на верхній регістр
print(result.islower())  # перевірка на нижній регістр
