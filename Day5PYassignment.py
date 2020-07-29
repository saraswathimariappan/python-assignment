#!/usr/bin/env python
# coding: utf-8

# In[7]:



print("Sort increasing order but all zeros should be at right hand side")
a = ("0","1","2","10","4","1","0","56","2","0","1","3","0","56","0","4")
x = sorted(a)
print(x)


# In[8]:


print("list1 = [10,20,40,60,70,80] sorted list")
print("list2 = [5,15,25,35,45,60] sorted list")
print("merge these two sorted list produce one sorted list, but use only one loop either while or for only one time")
test_list1 = [10,20,40, 60,70,80]
test_list2 = [5,15,25,35,45,60]
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))
res = sorted(test_list1 + test_list2)
print("the combined sorted list is " + str(res))


# In[ ]:




