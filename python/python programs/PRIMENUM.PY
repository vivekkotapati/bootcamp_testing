
#if the natural number is greater than 1 and having no positive divisors other than 1 and the number itself etc


def PrimeCheck(n):
    # check given number is more than one
    if n > 1:
        # iterate the given number with for loop
        for i in range(2,n):
            # check given number is divisible or not
            if(n % i) == 0:
                print(n,"is not prime num")
                break
        else:
            print(n,"is a prime number")
    else:
        print(n,"is not a prime number")
        
# take input from user
n = int(input("enter a nummber:"))
PrimeCheck(n)


'''
num = int(input("enter a number:"))
# define a flag variable
flag = False

if num == 1:
    print(num,"is not a prime number")
elif num > 1:
    #check factors
    for i in range(2,num):
        if (num % i) == 0:
            flag = True
            break
    # check if flag is true
    if flag :
        print(num,"is not  a prime number")
    else:
        print(num,"is a prime number")
'''


#find prime numbers within range
'''
lower = 1
upper = 100
print("prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
    if num > 1:
        for i in range(2,num):
            if(num % i) == 0:
                break
        else:
            print(num)
''' 