class Vehicle:
    def gen_usage(self):
        print("general use: transportation")

class Car(Vehicle):
    def __init__(self):
        print("this is a car")
        self.wheels=4
        self.has_roof=True

    def spec_use(self):
        print("vacation with family")

class motorcycle(Vehicle):
    def __init__(self):
        print("this is a motorcycle")
        self.has_roof=False
        self.wheels=2

    def spec_use(self):
        print("ride, road trip")

c=Car() #instances
c.gen_usage()
c.spec_use()

m=motorcycle() #instances
m.gen_usage()
m.spec_use()

print(isinstance(c,Car))
print(isinstance(m,motorcycle))

print(issubclass(Car,Vehicle))
