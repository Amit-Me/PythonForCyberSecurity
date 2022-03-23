# String is immutable
# Above line means string does not support item assignment

name = "Jhon"

# We can not do name[0]='c'

# It can be accessed by indexes but can not changed by indexes(immutable)

print(name[2])      #This will print 'o' as output

# But we can change a string as whole like

name = "Smith"

# In python string can also be decleared as follows

a = name1 = "Jack"


### To concatinate two strings 

F_name = "Jack"
L_name = "Smith"
Full_name = F_name + " " + L_name
print(Full_name)

### To store same stuff in reapeting manner as string

Str = "A"*20
print(Str)

# There is a concept of slicing in which we can break string
### To do so we uses following syntax
### string[start:end:steps]
print(Full_name[3:7:1])


### To convert integer into string

i = 10
k = str(i)
print(k)

### To convert string into integer

a = "29"
print(int(a))

########### String Methods ###############

### To find any substring from a string we use string.find() method
# This method return starting index of the given substring 
# It is casesensitive
# If not found then return '-1"
Full_name = "Jack Smithiii"
print(Full_name.find("ck"))

### To replace particular substring from a string 
# Syntax of replacing any substring is
# string.replace(oldvalue,newvalue,count)  where count is the number 
# .. of how much time the change will occure
# .. Bydefault count is 1 and it can be ignored
Full_name.replace("Smith","Kal",1)
print(Full_name)