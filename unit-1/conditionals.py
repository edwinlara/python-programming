
'''
num = 7

if num > 5:
    print('too high')
elif num < 3:
    print('too low')
else:
    print('just right')

#print letter corresponding letters for grades
# 80 - 100, print 'A'
# 79 - 60, print 'B'
# 50 - 59, print 'C'
# 0 - 49, print 'F'

num = 80

if (num >= 80) and (num <= 100):
   print('A')
elif (num >= 79) and (num <= 60):
   print('B')
elif (num >= 50) and (num <= 59):
   print('C')
elif (num >= 0) and (num <= 49):
   print('F')
else
   print('default')

grade = 55

if grade >= 80:
    print('A')
elif grade >= 60:
    print('B')
elif grade >= 50:
    print('C')
else:
    print('F')



#fizzbuzz
#for the first 50 integers
#if its a multiple of 3, print 'fizz'
#if its a multiple of 5, print 'buzz'
#if its a multiple of 15, print 'fizzbuzz'
#otherwise, just print the number


for num in range(1, 51):
    print(num, end=' ')

for num in range(1, 51):
    if num % 3 == 0: #range is in num and modulas is seeing if there is a remainder in multiples of 3
        print('fizz')
    if num % 5 == 0:
        print('buzz')
    if num % 15 == 0:
        print('fizzbuzz')
    else:
        print(num)

for num in range(1, 51):
    if num % 15 == 0: 
        print('fizzbuzz')
    elif num % 5 == 0:
        print('buzz')
    elif num % 3 == 0:
        print('fizz')
    else:
        print(num)

name = 'Fizzbuzz'

if len(name) > 4:
    print('longer than 4')

if len(name) > 6
    print('longer than 6')



#with and everything has to be true if anything else than false
#divided any even number the remainder is 1

#using 'and' and 'or' in conditionals
num = 14

#display a message if number is odd and also less than 20
if num % 2 == 1 and num < 20:
    print('odd number less than 20')
else:
    print('something else')


num = 6
if num % 2 == 1:
    print('Weird')
if num % 2 == 0 and num >= 2 and num <= 5:
    print('Not Weird')

if num % 2 == 0 and num >= 6 and num <= 20:
    print('Weird')
if num % 2 == 0 and num > 20:
    print('Not Weird')


#group print statements together
if num % 2 == 1 or (num % 2 == 0 and num >= 6 and num <= 20):
   print('Weird')
if (num % 2 == 0 and (num >= 2 and num <= 5)) or  (num % 2 == 0 and num > 20):
    print('Not Weird')

'''

#nested ifs
city = 'Toronto'
name = 'Edwin'
if city == 'Toronto':
    if name == 'Princeton'
        print('Welcome, newcomer!!')
    elif name == 'Connor':
        print('Wassup!!')
    else:
        print('hello {}'.format(name))
else:
    print('I\'m not familiar with your city')