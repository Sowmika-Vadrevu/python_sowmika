#prgm to check the user entered num is a prime number or not
n=int(input("enter n "))
for i in range (2,n):
    if(n%i==0):
        print("not a prime")
        break
else:
    print("prime")
       
    