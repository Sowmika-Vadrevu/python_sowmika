#prgm to swap two numbers by taking the input frm the user using arithematic operator
n1=int(input("enter n1 "))
n2=int(input("enter n2 "))
print("before swapping n1=",n1,"n2=",n2)
n1=n1+n2
n2=n1-n2
n1=n1-n2
print("after swapping n1=",n1,"n2=",n2)