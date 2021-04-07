num_1=int(input("enter first number:"))
num_2=int(input("enter first number:"))
num_3=int(input("enter first number:"))
if num_1 < num_2 and num_3 < num_2:
    print("num 2 is the gretest number:",num_2)
    if num_2<num_1 and num_3<num_2:
        print("The sum of the gretest number and the lowest nomber is :",num_1+num_3)
elif num_2 < num_1 and num_3 < num_1:
    print("num 2 is the gretest number:",num_1)
    if num_1<num_2 and num_3<num_1:
        print("The sum of the gretest number and the lowest number is:",num_2+num_3)
    #(num_3<num_3 and num_2<num3):
else:
    print("num 3 is the gretest number:",num_3)
    print("the sum of the gretest number and the lowest number is:",num_1+num_2)
