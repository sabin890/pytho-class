# def func(*args):
#      print(args)
#     #  print(type(args))
# func(1,2,"sabin",4,3)

# def func(*args,**kwargs):
#     print(args,"\n",kwargs)
# func(1,2,3,"sabin",name="ram",contact="98238080",address="kathmandu")

# def welcome():
#     print("hello word")
# w=welcome# call by reference
# print(w)
# w()

# def w
# def namestae(name):
#     print(f"namestae{name}")
# def welcome(name):
#     print(f"welcome{name}")
# def greet(name,f):
#     f(name)
#     greet(namestae,"ram")
#     greet(welcome,"harry")

# def main():
#     def inner_function():
#         print("i am inner function")
#     inner_function()
# main()


# def main():
#     def inner_function():
#         print("i am inner function")
#     return inner_function
# f=main()
# f()
# f()


# def function(b):
#     def addition(a,b):
#         return a+b
#     def subtraction(a,b):
#         return a-b
#     if b == 1:
#         return addition
#     elif b == 2:
#         return subtraction
# add = function(1)
# print(add(10,3))

# sub=function(2)
# print(sub(10,3))


# num=10
# def func():
#     global num
#     num=num + 1
#     print(num)
# func()

# alist = [1,2,3,"sabin",2]
# def func():
#     alist.append("hari")
# print(alist)
# func()
# print(alist)

# def main():
#     num=11
#     def inner_function():
#         nonlocal num
#         num=num+1
#         print(num)
#     inner_function()
# main()