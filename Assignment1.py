#!/usr/bin/env python
# coding: utf-8

# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple
# of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
# comma-separated sequence on a single line.

# In[5]:


for i in range(2000,3201):
    if i%7 == 0 and i%5!=0:
        print(i,end=',')


# 2. Write a Python program to accept the user's first and last name and then getting them printed in
# the the reverse order with a space between first name and last name.

# In[6]:


fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print (lname + " " + fname)


# 3. Write a Python program to find the volume of a sphere with diameter 12 cm.
# Formula: V=4/3 * π * r
# 3

# In[10]:


pi = 3.1415926535897931
r= 12
V= 4/3*pi* r**3
print('The volume of the sphere is: ',V)


# 4. Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list.

# In[18]:


values = input("Please provide sequence of comma-separated numbers ")
l = values.split(",")
print(l)


# 5. Create the below pattern using nested for loop in Python.
# 
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# In[19]:


print("Program to print start pattern: \n");

rows = input("Enter max star to be display on single line ")
rows = int (rows)
for i in range (0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range (rows, 0, -1):
    for j in range(0, i -1):
        print("*", end=' ')
    print("\r")


# 6.
# Write a Python program to reverse a word after accepting the input from the user.
# 
# Input word: Ineuron
# 
# Output: noruenI

# In[16]:


x = input("Enter input string ")
string = x[::-1]
print(string)


# 7 .Write a Python Program to print the given string in the format specified in the sample output.
# WE, THE PEOPLE OF INDIA, 
# having solemnly resolved to constitute India into a
# SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
# its citizens

# In[17]:


print("WE, THE PEOPLE OF INDIA,\n\thaving solemnly resolved to constitute India into a SOVEREIGN,! \n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\t and to secure to all its citizens")


# In[ ]:




