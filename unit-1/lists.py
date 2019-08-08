'''

classmates = ['Connor', 'Efe', 'Alexander', 'Bianca', 'Edwin', 'Greg']

#print a list
print(classmates)

#numberr of items in a list -- use the functions len
print(len(classmates))

#get a specific item - the first
print(classmates[0])

#print last element
#print(classmates[len(classmates) - 1])

#shortcut for last element
#print(classmates[-1])

#slicing - taking sections of the list
#print(classmates[0:3])

#adding an element to the end of a list
classmates.append('Edwin')

print(classmates)

#remove from end of the list
classmates.pop()

print(classmates)

#inserting at a specific position
classmates.insert(0, 'Edwin')

print(classmates)

#remove an element
classmates.remove('Edwin')

print(classmates)

'''
#age single and ages in plural convention 

#calculate the sum of a list of numbers
ages = [15, 25, 30, 27, 29, 41, 23, 20, 31, 19]

total_ages = 0

'''
#use a for loop
total_ages = 0
for age in ages:
    total_ages += age #total_ages + age

print(total_ages) 

'''


'''
#another for loop - use range and indexes
for idx in range(len(ages)):
    total_ages += ages[idx]

print(total_ages)




#print(sum(ages))

#calculate the sum of all the odd number ages in the list


if num % 2 == 1:
    print(total_ages)




if total_ages % 2 == 1:
for age in ages:
    total_ages += age #total_ages + age

print(total_ages)


for idx in range(len(ages)):
    total_ages += ages[idx]


    '''

for age in ages:
    if age % 2 == 1:
        total_ages += age

print(total_ages)




