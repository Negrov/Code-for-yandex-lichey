class BoundingRectangle:

    def __init__(self):
        self.points = list()

    def add_point(self, *point) -> None:
        self.points.append([point[0], point[1]])
        return

    def width(self) -> int:
        x = [i[0] for i in self.points]
        return max(x) - min(x)

    def height(self) -> int:
        y = [i[1] for i in self.points]
        return max(y) - min(y)

    def bottom_y(self) -> int:
        return min([i[1] for i in self.points])

    def top_y(self) -> int:
        return max([i[1] for i in self.points])

    def left_x(self) -> int:
        return min([i[0] for i in self.points])

    def right_x(self) -> int:
        return max([i[0] for i in self.points])
