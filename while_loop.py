#Bounded Loop
    #Which has fixed boundary
    #which has starting and ending point fixed
    #for loop is good for it 
#Unbounded Loop
    #No fix boundary
    #while loop



choice="y"
while choice=="y":
    num_1=int(input("enter a number:"))
    num_2=int(input("enter a number:"))
    print(f"sum of{num_1} and {num_2} is {(num_1+num_2)}")
    choice=input("want to continue:if you want to continue type: yes--> y--<<>>--otherwise type no: No--> n")