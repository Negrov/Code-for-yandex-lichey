"""


Реализуйте класс Rectangle для описания прямоугольника, стороны которого параллельны осям координат.

При инициализации экземпляра передаются координаты левой нижней точки прямоугольника x и y, а также его ширина и высота
w и h. Таким образом, координаты верхнего правого угла — (x + w) и (y + h).

При вызове метода intersection (например, rect1.intersection(rect2)) должен возвращаться прямоугольник, который
возникает как пересечение rect1 и rect2. Если прямоугольники не пересекаются, должен возвращаться объект None.

Также необходимо реализовать метод get для каждого из атрибутов класса, возвращающий заданное значение данного атрибута.
Пример: get_*() - возвращает значение атрибута *.

Гарантируется, что во входных данных ширина и высота любого прямоугольника положительны.

Если пересечением прямоугольников является точка или отрезок, то следует считать, что они не пересекаются.

    Формат ввода

Каждый тест представляет собой код, в котором будут использоваться ваш класс.
Файл c решением не обязательно называть solution.py, он будет переименован автоматически.
Тест запускается с вашим классом, а его вывод сравнивается с правильным решением.

"""


class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def intersection(self, other):

        if ((other.x >= self.x + self.w) or (other.y >= self.y + self.h) or
                (self.x >= other.x + other.w) or (self.y >= other.y + other.h)):
            return None

        else:
            dub = Rectangle(0, 0, 0, 0)
            dub.x = max(self.x, other.x)
            dub.w = min(self.x + self.w, other.x + other.w) - dub.x
            dub.y = max(self.y, other.y)
            dub.h = min(self.y + self.h, other.y + other.h) - dub.y
            return dub

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def get_w(self) -> int:
        return self.w

    def get_h(self) -> int:
        return self.h
