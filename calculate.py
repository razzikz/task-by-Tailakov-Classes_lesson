class Calc:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def multy(self):
        return self.x * self.y

    def minus(self):
        return self.x - self.y

    def division(self):
        try:
            return self.x / self.y
        except ZeroDivisionError:
            return "bonfire you!"


num = Calc(int(input("x: ")), int(input("y: ")))
print(num.division())
print(num.minus())
print(num.add())
print(num.multy())