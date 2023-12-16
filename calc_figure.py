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


print("Your choice: (1 - circle, 2 - square, 3 - triangle)")
choice = int(input())
try:
    if 1 >= choice <= 3:
        if choice == 1:
            num = Calc(0, 0, 0, int(input("radius: ")))
            print(f'S: {num.circle()}')
        elif choice == 2:
            num = Calc(int(input("a: ")), int(input("b: ")), 0, 0)
            print(f'S: {num.square()}')
        elif choice == 3:
            num = Calc(int(input("b: ")), 0, int(input("h: ")), 0)
            print(f'S: {num.triangle()}')
except ValueError:
    print('Try once more')