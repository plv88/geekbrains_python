# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

data = open("data_test.txt", "w")
while(True):
    input_string = input("Введите данные")
    if input_string == "":
        break
    data.writelines(input_string+'\n')
data.close()
print("Запись завершена, можно посмотреть что записали")