# Unicode is a extend form of ASCII 
# Because in ASCII only 128 code points are there 
# But in unicode 1114112 (17 * 2^16 - 1) code points are possible
# First 128 are ASCII and other are extended code points
### To know more about unicode visit https://docs.python.org/3/howto/unicode.html

###### Decleration of unicode string
#name = u'Jhon'

###### Conversion of string to unicode and vv
name = "Jhon"
print(name.encode('utf-8'))     # From string to Unicode
name = u'U+1F600'
print(type(name))
print(name)
#print(name.decode('utf-8'))

