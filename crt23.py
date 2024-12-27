# prgm to check whether the user entered integer is a prime palindrome or not
n=int(input("enter n "))
x=True
for i in range(2,n):
    if(n%i==0):
        print("not a prime palindrome!!!")
        x= False
        break
    
else:
    x= True    
if (x==True):
        t=n
        rem=0
        rev=0
        while(n!=0):
            rem=n%10
            rev=rem*10+rem
            n=n//10
        if(rev==t):
            print("prime palindrom <3") 
        else:
            print('prime but not palindrome')  