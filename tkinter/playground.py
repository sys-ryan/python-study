def add(*args):
    total = 0
    for n in args:
        total += n
    print(total)


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]

    print(n)


calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan")

print(my_car.make)
print(my_car.model)