#!/usr/bin/env python
# coding: utf-8

# sum of n numbers

# In[6]:


num=int(input("enter the number"))
i=1
sum=0
while(i<=num):
    sum=sum+i
    i=i+1
print("sum is", sum);


# prime or not

# In[7]:


def check(n, div = None):
    if div is None:
        div = n - 1
    while div >= 2:
        if n % div == 0:
            print("Number not prime")
            return False
        else:
            return check(n, div-1)
    else:
        print("Number is prime")
        return 'True'
n=int(input("Enter number: "))
check(n)


# In[ ]:




