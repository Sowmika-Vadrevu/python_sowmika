#sum of even numbers nd odd numbers
n=int(input('enter the number: '))
even=0
odd=0
for i in range(1,n+1):
    if(i%2==0):
        even+=i
    else:
        odd+=i
print(even,odd)        