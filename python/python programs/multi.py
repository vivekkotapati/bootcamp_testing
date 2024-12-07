'''n = int(input("enter a number:"))        
counter = 1      
# we will use a while loop for iterating 10 times for the multiplication table        
#print("The Multiplication Table of: ", num)      
while counter <= 20: # specifying the condition  
    ans = n * counter 
    counter += 1     
    print (n, 'x', counter, '=', ans)      
   # counter += 1
'''
n = int(input("Enter a number: "))
for i in range(1, 21):
    print(f"{n} x {i} = {n*i}")
