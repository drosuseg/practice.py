class Employee:

    def __init__(self,name,postion):
        self.name = name
        self.position = postion
    
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manager", "Cashier","Cook","Janitor"]
        return position in valid_position

employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Megan", "Cashier")
employee3 = Employee("Mark", "Cook")
employee4 = Employee("Bruce", "Janitor")

print(Employee.is_valid_position("Cashier"))
print(employee1.get_info(),employee2.get_info(),employee3.get_info())