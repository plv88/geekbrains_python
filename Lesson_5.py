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

name_lessons = open("ex_6_lessons.txt", "r", encoding="utf-8")
lesson_dict = {}
for line in name_lessons:
    line = line.replace("\n", "")
    lesson_list = line.split(":")
    lesson_list_hour = lesson_list[1].split(" ")
    sum_lesson = 0
    for el in lesson_list_hour:
        if "(" in el:
            hour_list = el.split("(")
            sum_lesson += int(hour_list[0])
    lesson_dict[lesson_list[0]] = sum_lesson
print(lesson_dict)
name_lessons.close()