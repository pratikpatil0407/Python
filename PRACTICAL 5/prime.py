n=int(input("Enter number:"))

def prime(n):
    if(n==0 or n==1):
        return 0
    else:
        for i in range(2,n//2):
            if(n%i==0):
                return 0
            break
if(prime(n)==0):
    print(n," is not a prime number")
else:
    print(n," is a prime number")