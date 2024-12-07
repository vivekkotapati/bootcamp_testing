# swap of two numbers using temp variable

x = 4
y = 3
print('value before swap of x:',x)
print('value before swap of y:',y)
# create temp variable and swap

temp = x
x = y
y = temp

print('the value of x after swaping: {}'.format(x))
print('the value of y after swaping: {}'.format(y))

#without using temp variable by using comma(,) operator

a = 10
b = 20

a,b = b,a

print("a=",a)
print("b =",b)

# to swap the values using xor
a = int(input("enter a value of a:"))
b = int(input("enter a value of b:"))

a = a ^ b
b = a ^ b
a = a ^ b

print("the value of a after swap:",a)
print("the value of b after swap:",b)

# swap using arthimetic operator

a = int(input("enter value of a:"))
b = int(input("enter value of b:"))

a = a + b #a = a*b
b = a - b #b = a/b  using multipilication and division oper
a = a - b #a = a/b

print("the value of a after swap:",a)
print("the value of b after swap:",b)

# swapcase() in string convert lowercase() to uppercase()

viv = "hi Hello"
print(viv.swapcase())



