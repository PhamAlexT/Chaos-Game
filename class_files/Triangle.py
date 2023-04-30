from Point import Point


class Triangle():
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def get_p1(self):
        return self.p1

    def get_p2(self):
        return self.p2

    def get_p3(self):
        return self.p3

    def get_points(self):
        return [self.p1, self.p2, self.p3]

    def __str__(self):
        res = "Triangle defined with:\n"
        res += "\n".join(self.get_points())
        return res
