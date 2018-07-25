'''
import myFile   
letters=['a','c','d','w']
result=myFile.find_index(letters,'w')
print(result)

import myFile as mf
letters=['a','c','d','w']
result=mf.find_index(letters,'a')
print(result)
'''

from myFile import find_index,test # import * for everything
letters=['a','c','d','w']
result=find_index(letters,'d')
print(result)
print(test)

import sys
print(sys.path)  #i add my module path in bash profile i can see the path
import cus_mod_file # or sys.path.append('/Users/ozanocak/Desktop/python/My-Modules')

import random,math,os
random_letters=random.choice(letters)
print(random_letters)

rads=math.radians(90)
print(rads)
print(os.getcwd())
print(os.__file__)