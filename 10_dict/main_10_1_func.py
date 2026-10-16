# Функції для роботи з словниками
person = {"name": "Atmos", "age": 15, 5: 12, True: "boolean", (3, 5): 45}
# print(person.get("name"))

# person.clear()  # Повне очищення словника
# person.popitem()  # Видалення останнього елементу
# person.pop("age")  # Видалення окремого ключа
person["bio"] = "Text"  # Додавання елементу в словник
print(person)
