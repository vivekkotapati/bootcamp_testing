# to check leap year

def CheckLeap(year):
    if((year%400 == 0) or
       (year%100!=0) and
       (year%4==0)):
        print("year is leap year");
    else:
        print("given year is not a leap year");
#taking input from user

year = int(input("enter a num:"))
CheckLeap(year)