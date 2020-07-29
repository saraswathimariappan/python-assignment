#!/usr/bin/env python
# coding: utf-8

# In[3]:



test_keys = ["a","b","c","d","e"] 
test_values =  [1,2,3,4,5,7,8]
  

print ("Original key list is : " + str(test_keys)) 
print ("Original value list is : " + str(test_values)) 
  

res = {test_keys[i]: test_values[i] for i in range(len(test_keys))} 
  

print ("Resultant dictionary is : " +  str(res)) 


# In[ ]:




