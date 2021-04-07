y="yes"
while y=="yes":
    
    years=int(input("enter  year:"))
    if years>=1000 and years<=9999:
        if years%4==0 and years%100!=0:
            print(f"{years} is a leap year")
        elif years%100==0:
            print(f"{years} is not a leap yera")
        elif years%400==0:
            print(f"{years} is a leap year")
        else:
            print(f"{years} is not a leap year")
    else:
        print("input year most be 4 digits")
    y=input("enter yes if you want to continue:")
    