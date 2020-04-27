class Car:
    # Properties
    color = ""
    brand = ""
    number_of_wheel = 4
    number_of_seats = 4
    maxspeed = 0
    # Contructor

    def __init__(self, color, brand, number_of_wheel, number_of_seats, maxspeed):
        self.color = color
        self.brand = brand
        self.number_of_wheel = number_of_wheel
        self.number_of_seats = number_of_seats
        self.maxspeed = maxspeed

    def setcolor(self, x):
        self.color = x

    def setbrand(self, x):
        self.color = x

    def setspeed(self, x):
        self.color = x

    def printdata(self):
        print("Color of thiscar is ", self.color)
        print("brand of this car is", self.brand)
        print("Max speed of this car is ", self.maxspeed)

    def __del__(self):  # Decontructor
        print()
