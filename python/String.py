'''
  collection of char
'''
'''a='vivek'
b="vicky"
c=''''''


print(type(a),type(b),type(c))'''
'''
lower()
upper()
endswith()
replace()
index()
count()
remove prefix()
remove suffix()
split()
strip()
rstrip()
lstrip()
'''
'''
str="vivek"
str1="VIVEK"           #lower and upper
print(str.upper())
print(str1.lower())
 '''

str="viv kotapati"
print(str.endswith("kotapati"))
print(str.startswith("v"))

str="Java python"
print(str.replace("python","program"))

str="Java python"
print(str.index("v"))       #index and find
print(str.find("python"))


str="Java python"
print(str.count('a'))                 #count,prefix,suffix
#print(str.removeprefix("Java"))
print(str.removesuffix("python"))

#str="  vivek"
#print(str)
#print(len(str))     #strip,lstrip,rstrip
#a=str.lstrip()
#print(len(a))
'''
str="vivek  "
print(str)
print(len(str))     #strip,lstrip,rstrip
a=str.rstrip()
print(len(a))
'''

a = "vivek" #array
print(a[2])
print(len(a)) #lenght of string

'''
for x in "vivek":
    print(x)
 '''  
'''
b="Hello world"  #reverse
print(b[::-1])  
print(b[2:5]) #index 2 to 5
print(b[:5]) #starting to upto index 5
print(b[2:]) #from index 2 to end

print(b[-5:-2]) # Negative slicing start from end with -1


a = "Hello,world"
#print(a.replace("H","v"))  #Replace()

#print(a.split(",")) #split() create space b/w words


# String Format

name = "vivek"
age = "22"
print(name+" "+age)
'''
'''
age = 18
note = "if your {} then u r eligible"  # using {} can format value
print(note.format(age))

a = "I am Vivek"
print(a.swapcase())  #swap upper to lower and lower to upper

'''
