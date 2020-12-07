# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.
#Записал на английском, в задании не было русские\английский поэтому чтобы не возиться с кодировкой, сделал английские.
my_employ = open("employees.txt", "r")
#Запишем все в словарик, так проще будет работать
individual_dict = {}
for line in my_employ:
    line = line.replace("\n", "")
    array_employ = line.split(" ")
    individual_dict[array_employ[0]] = array_employ[1]
sum = 0
n = 0
for keys, values in individual_dict.items():
    if int(values) < 20000:
        sum += int(values)
        n += 1
        print(keys)
print(f"Средняя тех кто зарабатывает меньше 20к - {int(sum/n)}")
sum = 0
n = 0
for keys, values in individual_dict.items():
    sum += int(values)
    n += 1
print(f"Средняя всех - {int(sum/n)}")

my_employ.close()
