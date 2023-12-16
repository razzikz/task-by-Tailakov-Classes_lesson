from functools import reduce
import math
# def S(h, r, p=math.pi):    return 2 * p * r * (r+h)
#
# print(S(float(input("height: ")), float(input("radius: "))))
#
# double = lambda x, y: x*y
# x = int(input())
# y = int(input())
# print(double(x, y))
#
# def not_lambda():
#     global x, y
#     return x*y
#
# print(not_lambda())
# my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
# # new_list = list(filter(lambda x: (x%2 == 0) , my_list))
# new_list = list(map(lambda x: x*2, my_list))
# summa = reduce((lambda x, y: x+y), my_list)
# print(new_list)
# print(summa)
# tables = [lambda x = i: x*10 for i in range(1, 11)]
# for table in tables:
#     print(table())
class Person:
    def __init__(self, name, age, work):
        self.name = name
        self.age = age
        self.work = work

    def say(self, message):
            print(message)

    def say_hello(self):
            self.say("Hello work")  # обращаемся к выше определенному методу say

    def info(self):
        print(f'Name: {self.name}\nAge: {self.age}\nWork: {self.work}')


john = Person('John', 12, 'school')
bob = Person('Bob', 67, 'none')

john.info()
bob.info()