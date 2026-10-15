# ---- Робота з текстом -----
text = "football,basketball,skate"
hobbies = text.split(',')

for i in range(0, len(hobbies)):
    print(hobbies[i])
    hobbies[i] = hobbies[i].capitalize()

result = ", ".join(hobbies)

print(hobbies)
print(result)
