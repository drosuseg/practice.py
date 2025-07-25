class Student:
 
 class_year = 2024
 class_num = 0

 def __init__ (self, name, age):
  self.name = name
  self.age = age
  Student.class_num += 1

student1 = Student("Don", 21)
student2 = Student("Rose", 20)
student3 = Student("Dros", 20)

print(f"My graduating class of {Student.class_year} has {Student.class_num} students")
print(student1.name)
print(student2.name)
print(student3.name)