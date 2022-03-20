#!/user/bin/python
name = "Jhon"
print("Address of name in memory : ", id(name))

#To print that address in Hexadecimal

print("The address of name in memory in hexadecimal form : ",hex(id(name)))

#Anothe way to get the memory address in hexamdecimal is :

print( name.__repr__)