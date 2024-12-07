#for i in range(1,11):
#    print(i)

#Write a program which prints all the divisors of a number.

n = int(input("Enter a num:"))
for i in range(2,n):
    if n % i == 0:
        print(i)
