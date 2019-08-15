
'''

#defining a function with no arguments

def first_functions():
    print('This is my first function')

#first_function()

def message(name):
    print('hello {} !! How are you?'.format(name))

#message('Edwin')

'''

'''

#define a function with two arguments
def send_greeting(name, is_student):
    suffix = ''
    if is_student:
        suffix = 'a student'
    else:
        suffix = 'an instructor'
    message = 'Hello {}, you are {}'.format(name, suffix)

    print(message)

#send_greeting('Edwin', True)

#print(message)

'''

'''
#global scope the whole thing vs local scope only in block
#define a function that returns a value
def sum_my_number(nums):
    total = 0
    for num in nums:
        total += num
    
    return total #use return to pass a value back to the calling function

result = sum_my_number([10, 12, 30, 40, 50])

print(result)

print(sum_my_number([1, 2, 3, 4, 5]))

'''

#can only use return when you use function
#talking about scope next class
#function next class
#try list intersections

def item_count(a_list, key):
    count = 0
    for item in a_list:
        if item == key:
           count += 1
    return count\

print(item_count([1, 2, 3, 4], 3))

print(item_count(['kiwi', 'mango', 'strawberry', 'kiwi', 'kiwi'], 'kiwi'))

#item_count([1, 2, 3, 2, 7], 2) - 2

#list intersection







