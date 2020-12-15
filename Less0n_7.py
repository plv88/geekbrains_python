# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.

# #так проще сложить списки, с циклами просидел несколько часов
from itertools import zip_longest

class Matrix:
    def __init__(self, number: list):
        self.matrix_list = number

    def __str__(self):
        self.element = []
        for el in self.matrix_list:
            self.element.append(" ".join([str(i) for i in el]))
            self.element.append("\n")
        return ("".join([str(j) for j in self.element]))

    def __add__(self, other):
        self.summ_element = []
        if len(self.matrix_list) == len(other.matrix_list):
            for i in range(len(self.matrix_list)):
                self.summ_element.append([x + y for x, y in zip_longest(self.matrix_list[i], other.matrix_list[i], fillvalue=0)])

        elif len(self.matrix_list) > len(other.matrix_list):
            for i in range(len(other.matrix_list)):
                self.summ_element.append([x + y for x, y in zip_longest(self.matrix_list[i], other.matrix_list[i], fillvalue=0)])
            self.finish_i = i+1
            self.count = len(self.matrix_list) - len(other.matrix_list)
            for j in range(self.count):
                self.summ_element.append(self.matrix_list[self.finish_i+j])

        elif len(self.matrix_list) < len(other.matrix_list):
            for i in range(len(self.matrix_list)):
                self.summ_element.append([x + y for x, y in zip_longest(self.matrix_list[i], other.matrix_list[i], fillvalue=0)])
            self.finish_i = i+1
            self.count = len(other.matrix_list) - len(self.matrix_list)
            for j in range(self.count):
                self.element_str = other.matrix_list[self.finish_i+j]
                for k in range(len(self.matrix_list)):
                    self.element_str.append(0)
                self.summ_element.append(self.element_str)
        else:
            print("Что-то не то")
        self.matrix_list = self.summ_element
        return Matrix.__str__(self)

m0 = Matrix([
    [1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2]
])
print(m0)
print("_________")
m1 = Matrix([
    [1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2]
])
m2 = Matrix([
    [10, 10, 10],
    [11, 11, 11],
    [12, 12, 12]
])
print(m1+m2)
print("_________")
m3 = Matrix([
    [10, 10, 10, 10, 10],
    [20, 20, 20, 20, 20],
    [30, 30, 30, 30, 30],
    [40, 40, 40, 40, 40]
])
m4 = Matrix([
    [10, 10, 10],
    [11, 11, 11],
    [12, 12, 12]
])
print(m3+m4)

# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
# одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
# классы для основных классов проекта, проверить на практике работу декоратора @property.


class Clothes():
    def __init__(self, title):
        self.title = title
        print(f"Название линейки одежды - {self.title}")

    def coat(self, size):
        self.size = int(size)
        self.coat_expense = self.size / 6.5 + 0.5
        return self.coat_expense

    def costume(self, growth):
        self.growth = growth
        self.costume_expense = 2 * self.growth + 0.3
        return self.costume_expense

    @property
    def expense(self):
        return f"Суммарный расход ткани состовляет: {self.coat_expense + self.costume_expense} ед."

wear = Clothes("Зима 2020")
print(wear.coat(250))
print(wear.costume(165))
print(wear.expense)

print("________________________________________")

from abc import ABC, abstractmethod

class Clothes_abc(ABC):
    def __init__(self, title, par=None):
        self.title = title
        self.par = par

    @abstractmethod
    def calc_expense(self):
        pass

class Coat(Clothes_abc):
    @property
    def calc_expense(self):
        self.coat_expense = (self.par / 6.5) + 0.5
        return self.coat_expense

class Costume(Clothes_abc):
    @property
    def calc_expense(self):
        self.costume_expense = 2 * self.par + 0.3
        return self.costume_expense

class Sum_expense():
    def __init__(self, par1, par2):
        self.par1 = par1
        self.par2 = par2

    def calc_expense(self):
        return self.par1 + self.par2

coat_abc = Coat("Пальто", 250)
print(coat_abc.calc_expense)
costume_abc = Costume("Зима 2021", 165)
print(costume_abc.calc_expense)
expense_all = Sum_expense(costume_abc.calc_expense, coat_abc.calc_expense)
print(expense_all.calc_expense())

# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны
# быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение
# (__mul__()), деление (__truediv__()). Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
# этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
# ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный
# метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет
# строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет
# строку: *****\n*****\n*****.

class Cell():
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        """Не сильно понимаю смысл от этого сложения, обычное сложение, без каких либо условий"""
        return self.count + other.count


    def __sub__(self, other):
        return self.count - other.count if (self.count - other.count) > 0 else "Клеточки не вычитаются"

    def __mul__(self, other):
        return self.count * other.count

    def __truediv__(self, other):
        return self.count // other.count if (self.count // other.count) > 0 else "Клеточки не делятся"

    def make_order(self, row):
        self.row = row
        self.number = self.count // self.row
        self.remain = self.count - (self.number * self.row)
        self.result = []
        for i in range(self.number):
            self.result.append("".join(["*" for x in range(self.row)]))
            self.result.append("\n")
        if self.remain > 0:
            self.result.append("".join(["*" for x in range(self.remain)]))
        return "".join(self.result)



cell_1 = Cell(22)
cell_2 = Cell(25)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))