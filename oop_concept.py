#1. class and object
#2. encapsulation
#3. Inheritance
#4. polymorphism
#5. abstraction
#6. access modifier
#7.accessor and mutator functions
# -->getter          --->setter

# class laptop:
#     #initializer function(initializer object)
#     def __init__(self,brand,colour,ram,rom):
#         self.brand=brand
#         self.colour=colour
#         self.ram=ram
#         self.rom=rom
#     def power_on(self):
#         print(f"{self.brand} laptop is starting")
#     def reboot(self):
#         print(f"{self.brand} is rebooting")
#     def about_brand(self):
#         print(f"{self.brand} laptop which have {self.colour} colour and {self.ram} ram")
# L=laptop("lenovo","black","16 GB","1TB")
# D=laptop("dell","red","8GB","1TB")
# D.power_on()
# L.power_on()
# L.about_brand()

# class calculate:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2

#     def add(self):
#         return self.num1+self.num2
#     def difference(self):
#         return self.num1-self.num2
#     def product(self):
#         return self.num1*self.num2
#     @staticmethod
#     def square_root(num):
#         return num**0.5

# c=calculate(19,12)
# print(c.add())  
# print(c.difference())
# print(c.product())
# print(c.square_root(100))
  

# class students:
#     college_name="abc college"
#     def __init__(self,id,name,contact):
#         self.id=id
#         self.name=name
#         self.contact=contact
# sd=students("001","sujan","982222")
# std=students("002","eshika","998889")
# print(students.college_name)
# print(sd.__dict__)
# print(std.__dict__)

# class product:
#     def __init__(self,name,price):
#         self.name=name
#         #product_price
#         #name managaling_classname__attrname
#         self.__price=price
#     @property
#     def price(self):
#         return self.__price
    
#     @price.setter
#     def price(self,price):
#         if price>0:
#         self.__price=price
#     pant=product("pant",1600)
#     #print(pant.get_price())
#     #pant.set_price(1700)
#     print(f"initial value:{pant.price}")
#     pant.price=900
#     print(f"final value:{pant.price}")
#     print(pant.__dict__)


#operator overloding

# class product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def __eq__(self,obj):
#         return self.price==obj.price
#     def __add__(self,obj):
#         return self.price+obj.price
# pant=product("pant",1600)
# tshirt= product("tshirt",1600)
# print(pant.__eq__(tshirt))
# print(pant+tshirt)   