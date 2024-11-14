num=int(input("Enter a number:"))

if(num<0):
    print(num," is negative")
elif(num>0):
    if(num<=100):
        print(num," is between 1 to 100")
    elif(num>100 and num<=200):
        print(num," is between 101 to 200")
    else:
        print(num," is greater than 200")
else:
    print(num," is zero")