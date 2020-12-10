# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный,
# желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
# завершать скрипт.


# import time
#
# class TrafficLight:
#     __color = ["красный", "желтый", "зеленный"]
#     def running(self):
#         print(TrafficLight.__color[0])
#         time.sleep(7)
#         print(TrafficLight.__color[1])
#         time.sleep(2)
#         print(TrafficLight.__color[2])
#         time.sleep(5)
#         print("Работа завершена")
#
# tr = TrafficLight()
# tr.running()
# print("___________________")
#
# class TrafficLight2:
#     __color = ["красный", "желтый", "зеленный"]
#     count = 0
#     def running(self):
#         print(TrafficLight2.__color[TrafficLight2.count])
#         if TrafficLight2.count == 0:
#             time.sleep(7)
#         elif TrafficLight2.count == 1:
#             time.sleep(5)
#         elif TrafficLight2.count == 2:
#             time.sleep(2)
#             TrafficLight2.count = -1
#         else:
#             print("Что-то сломалось")
#         TrafficLight2.count += 1
#
#
# tr2 = TrafficLight2()
# tr2.running()
# tr2.running()
# tr2.running()
# tr2.running()
# tr2.running()
# tr2.running()
# tr2.running()


# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
# массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса
# асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить
# работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

# class Road:
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#
#     def mass_of_asphalt(self, mass=None, height=None):
#         if mass is None and height is None:
#             print("Не заполнена масса и толщина асфальта")
#         elif mass is None:
#             print("Не заполнена масса")
#         elif height is None:
#             print("Не толщина асфальта")
#         else:
#             print(f"Масса асфальта равна {int(self._length * self._width * mass * height / 1000)} т")
#
# r = Road(20, 5000)
# r.mass_of_asphalt(25, 5)
#

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, wage, bonus, position=None):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        print(f"Полное имя сотрудника {self.surname} {self.name}.")

    def get_total_income(self):
        print(self._income["wage"] + self._income["bonus"])

p = Position("Андрей", "Иванов", 150000, 21000)
p.get_full_name()
p.get_total_income()