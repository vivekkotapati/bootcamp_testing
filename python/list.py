
a = [1,2,"vivek","uday",0.0,4,1,1]
print(a)
print(type(a)) # class of list
'''
b = [1,2,"vivek","uday",0.0,4]
print(b)
print((a == b))              # to check both list same or ordered

print(a[1:5:2])  # [start , stop , skip]
print(b[0:5:2])

print(a[::-1])
print(b[::-1])  # reverse list

print(a[2:5])
print(b[-5:-1]) # from -5 to end except -1

print(a[:-1])

print(a[-6:]) # complete list 

print(a)
'''
#append:always add element in last of list
a.append("python") 
print(a)

#extend(): to add all elements of one list to another list

a1=["vivek","bunny","jay"]
a.extend(a1)  
print(a)

# insert(): add element based on particular index, if index is greater than specific index it will be add last
# if index is lower than specific index then will be inserted at first position

n=[1,2,3,"vicky","rajesh"]
n.insert(2,"naresh")
n.insert(10,333)
n.insert(-9,111)
print(n) 

#remove():to remove specific element ,if specific element present multiple times then remove first occurance,
# if value not pressent raise ValueError

a.remove(2)
print(a)

#pop()
a.pop()# if index is not present then remove last element
a.pop(1) # pop removes elements based on index
print(a)




a = [1,2,"vivek","uday",0.0,4,1,1]
for i in a:         
    print(i)          # it prints one by one 

 

#a = [1,2,3,12,67,32,00]
#print(len(a))            # built in functions of list
#print(max(a))
#print(min(a))

'''
#Declaring the empty list    
l =[]    
#Number of elements will be entered by the user      
n = int(input("Enter the number of elements in the list:"))    
# for loop to take the input    
for i in range(0,n):       
    # The input is taken from the user and added to the list as the item    
    l.append(input("Enter the item:"))       
print("printing the list items..")     
# traversal loop to print the list items      
for i in l:     
    print(i, end = "  ")   

'''
# repetition of list  
# declaring the list  

list1 = [12, 14, 16, 18, 20]  
                           # repetition operator * 
l = list1 * 2  
print(l)


#descending order

n=[10,40,30,70] # ascending order
n.sort() 
print(n)

n.sort(reverse=True) # descending order
print(n)

n.sort(reverse=False) # ascending order
print(n)