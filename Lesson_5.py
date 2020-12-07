# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

f_obj = open("exercise_2_test.txt", "r")
content = f_obj.read()
content_str = content.split("\n")
print(f"Количество строк {len(content_str)}")
f_obj.close()
print()
f_obj = open("exercise_2_test.txt", "r")
n = 1
for line in f_obj:
    number_word = len(line.split(" "))
    line = line.replace("\n", "")
    print(f"Cтрока {n} - {line} - слов: {number_word}")
    n +=1
f_obj.close()
