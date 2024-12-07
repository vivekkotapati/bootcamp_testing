
a = (1,22,3,2,)
print(type(a))   #type
# tupel methods len,count,min,max,sum,copy,sorted,index 
print(len(a))
print(min(a),max(a),sum(a))   #built in fun
print(sorted(a))
print(a[1])
b = (21,9,3)
print(a + b)     # concating two tuples

print(a * 2)  # repetition

for i in a:
    print(i) # iteration 

print(1 not in a)
print(1 in a) # checking elements using membership operator and identity


'''
t = ()   # empty tuple
print("Empty tuple:",t)

a = (4,3,1,6,2) # creating tuple with int
print("tuple with int:",a)

b = (21,"vivek",32)        # creating a tuple with different datatype
print("mixed tuple:",b)

c = ("vivvu",) # tuple with single element
print(type(c))

'''
#slicing in tuple

a = (1,2,3,"hi","hlo")
print("elements b/w 0 and 3:",a[0:3])
print("elements between 0 and -3:",a[-4])
print("elements b/w 0 and 3:",a[: :-1])
print("elements b/w 0 and 3:",a[:])
print("elements b/w 0 and 3:",a[::])

#Tuple packing and tuple unpacking
# we can create a tuple by packing a group of variables
a = 10
b = 20
c = 30
t=a,b,c # here a,b,c are packed into tuple t, this is nothing but tuple packing
print(t)

# tuple unpacking is reverse of tuple packing, we can unpack tuple and assign to different variables
t=(10,20,30)
t=a,b,c
print('a=',a,'b=',b,'c=',c) # at time of tuple unpacking the number of variables should be same otherwise return error