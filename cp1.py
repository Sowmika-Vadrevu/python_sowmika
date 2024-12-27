name=input('Enter your name: ')
s1=int(input('subject 1 marks: '))
s2=int(input('subject 2 marks: '))
s3=int(input('subject 3 marks: '))
print('Student Report Card: ')
print('----------------------')
print('student name: ',name)
print('Subject1 score: ',s1)
print('Subject2 score: ',s2)
print('Subject3 score: ',s3)
if(s1>=35 and s2>=35 and s3>=35 ):
    sum=(s1+s2+s3)
    avg=sum/3
    print('Total: ',sum)
    print('Average:',avg)
    if(avg>=90):
        print('Congratualtions you have qualified with 1st class')
    elif(avg>=75):
        print('Congratualtions you have qualified with 2nd class')
    elif(avg>=60):
        print('Congratualtions you have qualified with 3rd class')
else:
    print('Fail')