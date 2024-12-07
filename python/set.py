#s = {1,2,3,4,2,3,5,43,22,11,3333334}  # does not allow duplicates
#print(s)
#print(type(s))  # defining set

'''add()
   pop()
   update()
   remove()
'''

s = set(["Jan","feb","apr","may","june","july","aug","dec"])
print("\nthe original set:",s)
print(len(s))

s.add("mar")                     # similarly we use update() to add more number of data

print("modified set by add method:",s)
print(len(s))

s.update({"sept","oct","nov"})
print("updated set:",s)
print(len(s))

s.discard("viv")   # using discard() method , we can remove particular element in set and if that element does not exist, it does not return error
print(s)

s.remove("mar") # we can also use remove() method to remove specified element but if the element not in set then we get keyerror
s.discard("nov")
print(s)

s.clear()
print(s)

#SET operations

#union
s1 = {"mon","tue","wed","thur"}
s2 = {"thur","fri","sat","sun"}          # combines two diff set to another new set
print(s1.union(s2))


#intersection

s1 = {1,2,3,4,5}
s2 = {1,2,3}
print(s1.intersection(s2)) # print(s1&s2)

#difference
print(s1-s2) # in this same elements will remove in both set and print remaining elements in set 1

# issuperset()
s3={1,2,3,4,5,6}
s4={5,6}
print(s3.issuperset(s4)) # if all elements in 2nd set are in 1st set , return true or else false
# issubset()
print(s4.issubset(s3)) # if all elements of 2nd set are also in 1st set



