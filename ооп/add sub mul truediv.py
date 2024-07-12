class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Seconds must be integers')
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f'{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}'

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, '0')

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('second term must be int')
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        return Clock(self.seconds + sc)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        print('iadd')
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('second term must be int or ')

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        self.seconds += sc
        return self

    def __sub__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('terms must be int or class instances')
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds - sc)

    def __isub__(self, other):
        print('isub')
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('terms must be integers')
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        self.seconds -= sc
        return self

    def __mul__(self, other):
        print('mul')
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('terms must be int or instances of Class')
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds * sc)

    def __imul__(self, other):
        print('imul')
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('invalid')
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        self.seconds *= sc
        return self


c1 = Clock(1000)
c2 = c1 + 1000
print(c1.get_time())
