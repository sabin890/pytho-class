#child class "is a " parent class
# class Persone:
#     def __init__(self,name,contact):
#         self.name=name
#         self.contact=contact
#     def walk(self):
#         print(f"{self.name} is walking")

# class Student(Persone):
#     def __init__(self,name,contact):
#         super().__init__(name,contact)
# class Teacher(Persone):
#     def __init__(self,name,contact):
#         super().__init__(name,contact)
# te=Teacher("shyam","98988")
# stu=Student("ram","9888088")
# stu.walk()

class Bird:
    def __init__(self,name):
        self.name=name
    def fly(self):
        print(f"{self.name} can fly")
class Pigeon(Bird):
    def __init__(self,name):
        super().__init__(name)
class Ostrich(Bird):
    def __init__(self,name):
        super().__init__(name)
    def fly (self):
        print(f"{self.name} cannot be fly")
class HummingBird(Bird):
    def __init__(self,name):
        super().__init__(name)
    def fly(self):
        super().fly()
        print(f"{self.name} can also fly backward")

p=Pigeon("hgAGD")
p.fly()
O=Ostrich("GAUGEDI")
O.fly()
H=HummingBird("HSAGD")
H.fly()