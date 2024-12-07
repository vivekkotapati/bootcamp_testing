'''import os
os.mkdir('sunny') 
print('my sub dir')#to create a sub dir

import os
os.makedirs('sub1/sub2/sub3')#to create a multiple dirs
print('sub1 sub2 sub3 are created')

import os
os.rmdir('sunny') #remove dir 
print('Sunny dir was deleted')

import os
os.removedirs('sub1/sub2/sub3')#remove multiple dir
print('All 3 dirs sub1,sub2,sub3 are removed')

import os
os.mkdir('hi')

import os
os.rmdir('hi')

'''
import os
#print(os.getcwd) # to get current working Dir
#to change current working Dir in python
os.chdir("C:\\Users\\LENOVO\\OneDrive\\Desktop\\python\\python programs") # we should give path to which we want to change
print(os.listdir()) # to get sub dir
