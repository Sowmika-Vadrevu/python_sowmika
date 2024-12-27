#program to print the count of even nmbrs from 1 to n
count=0
n=int(input("enter the number "))
for i in range(1,n+1):
    if(i%2==0):
        count+=1
print(' the number of even numbers are ',count)