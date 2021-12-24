#Q1
class rectangle():
    def __init__(self , length , width ):
        self.length =length
        self.width = width
    def area(self):
        return self.width*self.length

rect1 = rectangle(10,6)
print("the area of the rectangle is : ",rect1.area())
#Q2
class vehicle():
    def __init__(self , max_speed ,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
#Q3
class Vehicle1:
    pass
#Q4
class bus(vehicle):
    pass

