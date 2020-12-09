# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный,
# желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
# завершать скрипт.
import time

class TrafficLight:
    __color = ["красный", "желтый", "зеленный"]
    def running(self):
        print(TrafficLight.__color[0])
        time.sleep(7)
        print(TrafficLight.__color[1])
        time.sleep(2)
        print(TrafficLight.__color[2])
        time.sleep(5)
        print("Работа завершена")

tr = TrafficLight()
tr.running()
print("___________________")

class TrafficLight2:
    __color = ["красный", "желтый", "зеленный"]
    count = 0
    def running(self):
        print(TrafficLight2.__color[TrafficLight2.count])
        if TrafficLight2.count == 0:
            time.sleep(7)
        elif TrafficLight2.count == 1:
            time.sleep(5)
        elif TrafficLight2.count == 2:
            time.sleep(2)
            TrafficLight2.count = -1
        else:
            print("Что-то сломалось")
        TrafficLight2.count += 1


tr2 = TrafficLight2()
tr2.running()
tr2.running()
tr2.running()
tr2.running()
tr2.running()
tr2.running()
tr2.running()
