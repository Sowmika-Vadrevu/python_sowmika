#prgm to read an input for principal amount rate of interest nd time to calculate the simple interest 
p=int(input('Enter the Principal amount: '))
t=int(input('Enter the Time: '))
r=int(input('Enter the Rate of INtereset: '))
s=(p*t*r)/100
print('The Simple INterest is: ',s)