import math


class Calc:
    def __init__(self, x, y, h, r):
        self.x = x
        self.y = y
        self.h = h
        self.r = r

    def circle(self):
        return math.pi * self.r ** 2

    def square(self):
        return self.x * self.y

    def triangle(self):
        return 0.5 * (self.x + self.h)

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


print("Your choice: (1 - circle, 2 - square, 3 - triangle, 4 - add, 5 - minus, 6 - multyply, 7 - division, 8 - exit)")
while True:
    choice = int(input())
    try:
        if 1 >= choice <= 8:
            if choice == 1:
                num = Calc(0, 0, 0, int(input("radius: ")))
                print(f'S: {num.circle()}')
            elif choice == 2:
                num = Calc(int(input("a: ")), int(input("b: ")), 0, 0)
                print(f'S: {num.square()}')
            elif choice == 3:
                num = Calc(int(input("b: ")), 0, int(input("h: ")), 0)
                print(f'S: {num.triangle()}')
            elif choice == 4:
                num = Calc(int(input("x: ")), int(input("y: ")), 0, 0)
                print(f'Result: {num.add()}')
            elif choice == 5:
                num = Calc(int(input("x: ")), int(input("y: ")), 0, 0)
                print(f'Result: {num.minus()}')
            elif choice == 6:
                num = Calc(int(input("x: ")), int(input("y: ")), 0, 0)
                print(f'Result: {num.multy()}')
            elif choice == 7:
                num = Calc(int(input("x: ")), int(input("y: ")), 0, 0)
                print(f'Result: {num.division()}')
    except ValueError:
        print('Try once more')
    if choice == 8:
        print("GoodBye!")
        break
