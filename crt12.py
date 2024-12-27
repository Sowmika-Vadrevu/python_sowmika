#prgm to print the number of odd digits present in the user entered integer
n=int(input('enter the value n: '))
count=0
rem=0
while(n!=0):
    rem=n%10
    if(rem%2!=0):
        count+=1
    n=n//10
print("no of odd digits are ",count) 