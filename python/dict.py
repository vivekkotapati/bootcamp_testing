'''
Dict = {"Name":"vivek","Age":20,"Salary":700000} # key value pair
print(Dict)
print(type(Dict))  # intializing dict and finding class 

#print(Dict[0]) # if we execute with index it get KeyError ,
               # no index and slicing in dict

print(Dict["Name"])  # So we USE KEY to Access VALUE
'''

# methods : get,keys,values,update,items

d = {"Name":"viv","Age":22,1:'NTR'}
print(len(d)) # len of d
print(d.get(1)) # it returns value of key 1

print(d.keys())  # return all keys in dict
for k in d.keys():
     print(k)

print(d.values()) # return all values in dict
for v in d.values():
     print(v)

print(d.items())  # it return all keys and values as a pair

d.update({1:22}) # same key assigned so it modify value
print(d)

d.update({2:3}) # now assigning different key so new pair is added to dict
print(d)

pop_key = d.pop(1)     # it removes the key with 1   
print(d)      



d.clear()  # it removes all items in dict
print(d)
d={1:"v","d":3}
for i in d:
    #print(i) #only keys
    print(d[i]) #only values

for i,j in d.items(): # key value pair at same time
    print(i,j)

d={"Name":"John","Age":29,"Salary":25000,"Company":"WIPRO","Name":"John"}        
for i,j in d.items():        
        print(i,j)
        
d1 ={100:'vivek',200:'raju',300:'bunny'}
d2=d1.copy() # to create a duplicate dict(cloned type)
print(id(d1))
print(id(d2))

dict={1:'v',2:'k',3:'s'}
dic ={'a':'apple','b':'bat'}
dict.update(dic)
dict.update([(11,'A'),(22,'B')])
print(dict)
