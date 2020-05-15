"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
сообщение и завершать скрипт.
"""

from time import sleep


class TrafficLight:

    def __init__(self, green: int):
        self.__color = {
            'Red': 7,
            'Yellow': 2,
            'Green': green,
        }

    def running(self):
        for color, countdown in self.__color.items():
            print(f'The light color is {color}')
            sleep(countdown)


tverskaya_cross = TrafficLight(5)
tverskaya_cross.running()
