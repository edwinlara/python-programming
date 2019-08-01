'''
#integer
age = 41

#float
gpa = 3.0

#boolean
has_kids = True

#check the type of a variable 
print(type(age))
print(type(gpa))
print(type(has_kids))

#check if a number is even

num = 10
if num % 2 == 0:
    print('It is even!')
else:
    print('It is odd')

'''

#comparison operators
# > - greater than
# < - less than
# >= - greater than or equal to
# <=  - less than or equal to
# == - equal to
# != not equal to 

# = assin to

#truthiness
x = 10  # a non zero value is truthy

y = 0 #zero or negative value is falsy

z = 'Python' # a string of non zero length is truth

p = '' # as string of zero is falsy

q = [] #an empty list is falsy

if  q:
    print('yes')
else:
    print('no')

