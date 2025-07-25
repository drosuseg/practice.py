class Animal:
    def __init__ (self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Mouse(Animal):
    def speak(self):
        print("Squeek")

dog = Dog("Scooby")
cat = Cat("Gar")
mouse = Mouse ("Mickey")

print(dog.name, dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()

print(cat.name, cat.is_alive)
cat.eat()
cat.sleep()
cat.speak()

print(mouse.name, mouse.is_alive)
mouse.eat()
mouse.sleep()
mouse.speak()
