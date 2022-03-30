# This is for defining different ways for string formating


## Like c language python also support %s,%d etc.
# This can be implemented as

num = 10
line = "The value of the num is %d" % num
print(line)

# &&&&&&

st = "Jack"
line = "The value entered in st is %s" %st
print(line)

# For multiple at a time
line = "The value of st and num are %s and %d" %(st,num)
print(line)