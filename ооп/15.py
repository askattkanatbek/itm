import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
)

class Point:
    def __init__(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

    @property
    def x1(self):
        return self._x1

    @x1.setter
    def x1(self, value):
        old_value = self._x1
        self._x1 = value
        logging.info(f'Изменение x1: {old_value} -> {value}')

    @property
    def x2(self):
        return self._x2

    @x2.setter
    def x2(self, value):
        old_value = self._x2
        self._x2 = value
        logging.info(f'Изменение x2: {old_value} -> {value}')

    @property
    def y1(self):
        return self._y1

    @y1.setter
    def y1(self, value):
        old_value = self._y1
        self._y1 = value
        logging.info(f'Изменение y1: {old_value} -> {value}')

    @property
    def y2(self):
        return self._y2

    @y2.setter
    def y2(self, value):
        old_value = self._y2
        self._y2 = value
        logging.info(f'Изменение y2: {old_value} -> {value}')

a = Point(1, 2, 10, 20)


a.x1 = 5
a.x2 = 15
a.y1 = 25
a.y2 = 35
