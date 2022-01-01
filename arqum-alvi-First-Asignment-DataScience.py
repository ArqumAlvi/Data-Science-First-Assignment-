#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")


# In[7]:


import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


# In[8]:


import platform

print(platform.python_version())


# In[9]:


r = float(input("Enter radius of circle: "))
a = 3.14159 * r * r
print("Area of circle =", a)


# In[10]:


fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)


# In[11]:


first=int(input("enter first number : "))

Second=int(input("enter second number : "))

print("sum of",first, "and",Second,"is",first+Second)


# In[ ]:




