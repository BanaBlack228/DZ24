#1 задание
names = ["Лена", "Ольга", "Ольга", "Лена", "Саша", "Егор", "Лена", "Игорь"]

name_count = {}

for name in names:
    if name in name_count:
        name_count[name] += 1
    else:
        name_count[name] = 1

print("Количество вхождений имен:")
for name, count in name_count.items():
    print(f"{name} -> {count}")

#2 задание

numbers = [23, 45, 76, 89, 5]

total_sum = sum(numbers)

total_product = 1
for number in numbers:
    total_product *= number

result_dict = {
    total_sum: total_product
}

print("Словарь:", result_dict)

#3 задание

names = ["Лена", "Ольга", "Ольга", "Лена", "Саша", "Егор", "Лена", "Игорь"]

unique_names = list(set(names))

print("Список уникальных имен:", unique_names)
print("Количество уникальных имен:", len(unique_names))
