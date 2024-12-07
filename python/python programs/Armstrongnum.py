# AN armstrong number is a positive integer 
# the sum of cubes of each digit of number is equal to number itself.
# exmaple:
''' 
 371 = 3*3*3 + 7*7*7 + 1*1*1
      =  27 + 343 + 1
      = 371 

'''

n = int(input("enter a number:"))

# intiliize the sum

sum = 0
# find sum of cube of each digit
temp = n
while temp>0:
 digit = temp % 10
 sum += digit ** 3
 temp //= 10

 #display result
if n == sum:
  print(n,"is a Armstrong num")
else:
 print(n,"is not an armstrong number")

 # armstrong number between certain intervals
'''
lower = 100
upper = 2000

for num in range(lower,upper + 1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp>0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
    if num == sum:
        print(num)
'''