class Vehicle:
    def __init__(self, name, mileage, capacity):
       print("inside constructor")
       self.name = name
       self.mileage = mileage
       self.capacity = capacity

    def fare(self):
        return self.capacity * 100
   
class Bus(Vehicle):

    def fare(self):
        return (self.capacity * 100) + (super().fare() * 10/100)
    
School_bus = Bus("School Volvo", 12, 50)
print("total bus fare is:", School_bus.fare())


