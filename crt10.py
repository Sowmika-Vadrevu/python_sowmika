#prgm to print the nmbr of digits present in the user entered integer
n=int(input('enter the integer value:'))
digitcount=0
while(n!=0):
    n=n//10
    digitcount+=1
print(digitcount,"digits")