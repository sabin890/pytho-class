# def sum(a):
#     def times(b):
#         return a+b
#     return times
# # answer=sum(10)
# # print(answer(10))

# def welcome():
#     print("welcome ram")
# welcome()

def division(function):
    def divide(n1,n2):
        if n2==0 or n1==0:
            return "zero cannot divided "
        else:
            return divide(n1,n2)
    return divide
@division
def answer(num1,num2):
    return num1/num2

print(answer(10,1))
print(answer(10,1))
