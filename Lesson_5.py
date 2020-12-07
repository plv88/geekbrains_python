# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.
import random as rdn


ex5_data = open("ex5_number.txt", "w", encoding="utf-8")
number_count = int(input("Введите сколько сгенерировать чисел?"))
string_list = []
for i in range(number_count):
    string_list.append(str(rdn.randint(1, 100)))
my_string_list = ' '.join(string_list)
ex5_data.write(my_string_list)
ex5_data.close()

sum_number = open("ex5_number.txt", "r", encoding="utf-8")
for list in sum_number:
    list_number_for_sum = list.split(" ")
    result_sum_list = [int(el) for el in list_number_for_sum]
    sum = sum(result_sum_list)
print(list_number_for_sum)
print(sum)
ex5_data.close()
