#prgm to swap two numbers by taking the input frm the user without using temp
n1=int(input('enter the number '))
n2=int(input('enter the number '))
print("before swapping: n1=",n1,"n2=",n2)
n1,n2=n2,n1
print('after swapping: ',n1,n2)