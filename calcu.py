def calcu(num_1,num_2,aa):
    if(aa=="add"):
        return num_1+num_2
    elif(aa=="diff"):
        return num_1-num_2
    else:
        return num_1-num_2

result=calcu(10,5,"diff")
print(result)
 