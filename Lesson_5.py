# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество
# занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

# name_lessons = open("ex_6_lessons.txt", "r", encoding="utf-8")
# lesson_dict = {}
# for line in name_lessons:
#     line = line.replace("\n", "")
#     lesson_list = line.split(":")
#     lesson_list_hour = lesson_list[1].split(" ")
#     sum_lesson = 0
#     for el in lesson_list_hour:
#         if "(" in el:
#             hour_list = el.split("(")
#             sum_lesson += int(hour_list[0])
#     lesson_dict[lesson_list[0]] = sum_lesson
# print(lesson_dict)
# name_lessons.close()

# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
# собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

with open("ex_7_firms.txt", "r", encoding="utf-8") as data:
    dict_firms = {}
    dict_mean_profit = {}
    dict_mean_loss = {}
    company_list = []
    sum_company = 0
    sum_loss = 0
    #Будем считать профитные компании
    n = 0
    # и убыточные
    m = 0
    for el in data:
        el = el.replace("\n", "")
        data_list = el.split(" ")
        profit = int(data_list[2]) - int(data_list[3])
        if profit > 0:
            sum_company += profit
            n += 1
        else:
            sum_loss += profit
            m +=1
        dict_firms[data_list[0]] = profit
    average_profit = sum_company / n
    average_loss = sum_loss / m
    dict_mean_profit["average_profit"] = average_profit
    dict_mean_loss["average_loss"] = average_loss
    # вот думаю на сколько я правильно добавил простым аппендом
    company_list.append(dict_firms)
    company_list.append(dict_mean_profit)
    company_list.append(dict_mean_loss)
print(company_list)
