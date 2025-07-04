class Vehicle:
        def max_speed(self):
            print("Max speed of the vehicle")
        def fuel_type(self):
              print("Fuel type: ")
class BMW(Vehicle):
        def max_speed(self):
            print("Average max speed of a BMW is 250 kmph")
        def fuel_type(self):
              print("Fuel type: Premium Unleaded")

class Ferrari(Vehicle):
        def max_speed(self):
            print("Average max speed of a ferrari is over 300 kmph")
        def fuel_type(self):
              print("Fuel type: premium gas")

car1 = BMW()
car2 = Ferrari()

car1.max_speed()  
car1.fuel_type() 

car2.max_speed() 
car2.fuel_type() 