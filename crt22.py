#prgm to print the prime numbers from 1 to n
n=int(input("enter n "))
for i in range(2,n+1):
    for j in range (2,i):
        if(i%j==0):
            break
    else:
        print(i)     
   
           