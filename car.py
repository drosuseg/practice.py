class Car: 
    def __init__ (self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    
    def drive(self):
        print(f"You are driving the {self.model}")
    
    def stop(self):
        print(f"You stop the car {self.model}")
    
car1 = Car("Mustang", 2024,"red", True)

car1.drive()
car1.stop()

