class Student:

    def __init__ (self, name,subject, numSub):
        self.name = name
        self.subject = subject
        self.numSub = numSub

    def __str__(self):
        return f"name: {self.name} gpa: {self.numSub}"
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __gt__(self,other):
        return self.numSub > other.numSub
    
    def __lt__(self,other):
        return self.numSub < other.numSub
    
    def __add__(self,other):
        return self.numSub + other.numSub
    
    def __contains__(self, keyword):
        return keyword in self.name or keyword in self.subject
    
    def __getitem__(self, key):
        if key == "name":
            return self.name
        if key == "subject":
            return self.subject
    
student1 = Student("Don","PE" , 1)
student2 = Student("Donn","Science", 1)


print("Science" in student2)
print(student1['subject'])