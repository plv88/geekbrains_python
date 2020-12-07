# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

file_number = open("ex4_dict.txt", "r", encoding="utf-8")
file_number_russian = open("ex4_dict_rus.txt", "w", encoding="utf-8")
dict_number_russian = {1: "Один", 3: "Три", 4: "Четыре", 5: "Пять", 2: "Два"}
for line in file_number:
    line = line.replace("\n", "")
    string = line.split()
    russian_number = dict_number_russian[int(string[2])]
    # можено было записать в string[0] новое значение и соединить join, но чет так показалось быстрее
    string_new = russian_number + " " + string[1] + " " + string[2] + "\n"
    #string_new = string[0] + " " + string[1] + " " + russian_number + "\n"
    file_number_russian.write(string_new)

file_number.close()
file_number_russian.close()

#перечитал задание, возможно нужно было получить One — один, Two — два и тд, если так, то все еще проще, чуть по-другому
#конкатенацию сделать и все. В цикле закоментировал, какой вариант нужен, такой и будем юзать)

