#prgrm to print the reverse num of user entered num
n=int(input('enetr n '))
rem=0
rev=0
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)