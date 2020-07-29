#!/usr/bin/env python
# coding: utf-8

# In[12]:


# initializing tup  

print("question 2")
test_tup = (1,2)
  
# printing original tuple 
print("The original tuple is : " + str(test_tup))  
  
# Tuple elements inversions 
# Using list() + sum() 
res = sum(list(test_tup)) 
  
# printing result  
print("The summation of tuple elements are : " + str(res))  


# In[21]:


print("question 1")
# initializing dictionary  
old_dict ={21:"FTP",22:"SSH",23:"TELNET",80:"HTTP"}

new_dict = dict([(value, key) for key, value in old_dict.items()]) 
  
# Printing original dictionary  
print ("Original dictionary is : ") 
print(old_dict)  

print() 

# Printing new dictionary after swapping keys and values 
print ("Dictionary after swapping is :  ")  
print("keys: values") 
for i in new_dict: 
  print(i, " :  ", new_dict[i]) 


# In[22]:


print("question 3")
   # List of tuples 
Input = [(14, 3),(23, 41),(33, 62),(1, 3),(3, 3)] 
 
# Find an element in list of tuples. 
Output = [item for item in Input 
         if item[0] == 3 or item[1] == 3] 
 
# printing output 
print(Output) 


# In[ ]:




