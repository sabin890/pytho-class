
a=int(input('enter first number:'))
b=int(input('enter second number:'))
c=int(input('enter third number:'))


print("the greatest number is")
if a>b and a>c:
    print(f"the greatest number{a}")
    if b<a and b<c:
        print(f"the smallest number is ={b}")
        print(f"the sum is:{b+a}")
    else:
        print(f"the smallest number is={c}")
        print(f"the sum is:{c+a}")
elif b>a and b>c:
    print(f"the greatest number{b}")
    if a<b and a<c:
        print(f"the smallest number is={a}")
        print(f"the sum number is={a+b}")
    else:
        print(f"the smallest number is={c}")
        print(f"the sum number is={c+b}")
else:
    print(f"the greatest number is={c}")
    if b<a and b<c:
        print(f"the smallest number is ={b}")
        print(f"the sum is={b+c}")
    elif a<b and a<c:
        print(f"the smallest number is={a}")
        print(f"the sum is={a+c}")