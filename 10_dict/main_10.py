# ---- dict -----

# print(person)
# print(person["age"])

# person[True] = "False"
# print(person[True])

person_1 = dict(name="Alex", age=14)
# print(person_1)
# print(person_1["name"])

# for key in person:
#     print(key)

# print(person.items())  # вивід значення ключ всього словника

person = {"name": "Atmos", "age": 15, 5: 12, True: "boolean", (3, 5): 45}

# for key, values in person.items(): # ключ значення
#     print(key, values, sep=" - ")

for el in person.values():  # Вивід лише значень
    print(el)

for el in person.keys():  # Лише ключ
    print(el)
