# prgm to print mul table frm 1 to n
n= int(input('enter the value of N : '))
for j in range (1,n+1):
    print("Multiplication Table of ",j,":")
    for i in range (1,11):
        print(j,"X",i,"=",j*i)
    
    print("------------------------------------------")
    
