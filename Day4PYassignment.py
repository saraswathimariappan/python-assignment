#!/usr/bin/env python
# coding: utf-8

# In[3]:


test_str = "what we think we become;we are Python programmer"
  
# initializing substring 
test_sub = "we"
  
# printing original string  
print("The original string is : " + test_str) 
  
# printing substring  
print("The substring to find : " + test_sub) 
  
# using list comprehension + startswith() 
# All occurrences of substring in string  
res = [i for i in range(len(test_str)) if test_str.startswith(test_sub, i)] 
  
# printing result  
print("The start indices of the substrings are : " + str(res)) 


# q1 above and q2 below

# In[6]:


test_str = "what we think we become;we are Python programmer"
test_str.isupper()


# In[7]:


test_str = "what we think we become;we are Python programmer"
test_str.islower()


# In[8]:


test_str = "what we think we become;we are python programmer"
test_str.islower()


# In[ ]:




