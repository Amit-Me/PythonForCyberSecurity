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

## One other way of string formating is by using "{}"
# Syntax for the same is 

print("My name is {} and my age is {}".format("Jack",10))
# And it can be done on index basis
# Syntax for the same is 
person = {'name': "Jack", 'age':10}
print("My name is {0} and my age is {1}".format(person['name'],person['age']))
print("My name is {0[name]} and age is {1[age]}".format(person,person))
print("My name is {0[name]} and age is {0[age]}".format(person))
# For a list
p = ["Jack",10]
print("My name is {0[0]} and age is {0[1]}".format(p))
# For arguments of a function this can be done as
class P():
    def __init__(self,name,age):
        self.name=name
        self.age=age
fun = P("Jack",10)
print("My name is {0.name} and age is {0.age}".format(P))


tag = "HTML"
text = "HE"
print("<{0}>{1}<{0}".format(tag,text))