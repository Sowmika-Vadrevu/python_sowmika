#prgm to check the year as input frm the user nd check if it is a leap year or non leap year
def is_leap(year):
    leap = False
    if(year%4==0 and year%100!=0):
        leap=True
    elif(year%4==0 and year%100==0):
        if(year%400==0):
            leap=True
        else:
            leap=False
    
    return leap
year = int(input("enter the year "))
print(is_leap(year))