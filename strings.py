# Strings in Python
print('Enter your string')
string=str(input())
print('Length of string:',len(string)) # Cal. Length of Str. use len()

# String Indexing
print('Enter any index number from 0 to',len(string)-1) # Last index: length-1
index=int(input())
print('At index',index,'there is:',string[index])

print('Enter any index from -1 to',-len(string)) # Last index: -length
index=int(input())
print('At reverse index',index,'there is:',string[index])

reverse=string[::-1] # Reverse a string with [::-1]

# Length of String = n
# Last Index of String = n-1 (because index start with 0)
# Last Reverse Index of String = -n (because rev. index start with -1)

# String Properties and Methods
print(string.split()) # inbuilt string methods
print(reverse.upper()) # inbuilt string methods
print(reverse.lower()) # inbuilt string methods

# String Slicing
print('Enter the Start index and End index and Jump index') # by default keep jump=1
start=int(input())
end=int(input())
jump=int(input())
print('Here is sliced string:',string[start:end:jump])


# String Formatting 

# .format() method)

# > Simple Formatting
text = 'Rahul'
print('Master {}'.format(text))

print('I {1} {2} {0}'.format('country','love','my')) # mention the index number, its optional

# > Complex Formatting
print('Enter you name: ')
name = str(input())
print('Enter your Town Name')
town = str(input())
print('Enter you state')
state = str(input())
print('I am {} from {}, {}'.format(name,town,state))

# > Float Formatting
num = 22/7
print('Result is {n:1.2f}'.format(n=num))

# f literal 
Newname = 'Rishabh'
Newtown = 'Surat'
print(f'My name is {Newname} and I am from {Newtown}')