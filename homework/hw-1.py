
'''

#add this parent/file to same level as unit-1

statement = 'homework is fun!'
num = 3

#range is 0 to 1 less than declared
#use an underscore when you don't care about variable
#loop to print statement num number of times

for _ in range(num):
    print(statement)

'''

'''

#print(statement * num)

num_list = [2, 4, 6, 8, 10]
num = 5

#does not change the list
#go through each element and multiply by num

for x in num_list:
    print(x * num)

print(num_list)

'''

'''

#index visits each position in the list
#goes through and times everything times 5
for idx in range(len(num_list)):
    num_list[idx] *= num

print(num_list)

'''

'''

#reverse a string 
#create a variable that is an empty string 
#add characters of old string one by on

my_string = 'This is a sentence'

reversed_string = ''

#range stops 1 before
#loop from last to first character
#going through each string and writing backwords
#review this at home
for idx in range(len(my_string) - 1, -1, -1):
    reversed_string += my_string[idx]

print(reversed_string)

'''

'''

#calculater
#read an operation (add, mul, div, sub)
#read two integers
#execute the opertion 

#read the operation, store it in a variable
op = input('Enter and operation[add, sub, mul, div]: ')

#read in first number
num1 = int (input('Enter the first number: '))
num2 = int (input('Enter the second number: '))

#calculate the result
result = None

if op == 'add':
    result = num1 + num2 
elif op == 'sub':
    result = num1 - num2
elif op == 'mul':
    result = num1 * num2
elif op == 'div':
    result = num1 / num2
else:
    print('Invalid operation')

print(result)

'''

'''

def list_intersection(list_one, list_two):
    #create a new list with only items in both first and second list
    result = []
    for item_one in list_one:
        for item_two in list_two:
            if item_one == item_two:
                result.append(item_one)
    
    return result

print(list_intersection([1, 3, 5, 7, 9], [3, 4, 5, 6, 11]))

'''

'''

def list_intersection(list_one, list_two):
    #create a new list with only items in both first and second list
    result = []
    for item in list_one:
        for item in list_two:
                result.append(item)
    
    return result

'''
'''

def reversed_lists(list_one, list_two):
    result = []
    for item in list_one:
        for item in list_two:
            result.append(item)
    for idx in range(len(reversed_lists) - 1, -1, -1):
        reversed_lists += list_one == list_two[idx]
    return reversed_lists

print(intersection_lists)

'''

'''

def reverse_list(my_list):
    result = []
    for idx in range(len(my_list)-1, -1, -1): #range function start, stop, step
        result.append(my_list[idx])
    return result

#print(reverse_list(['apple', 'peach', 'strawberry', 'kiwi']))

#add apend or insert
#returns a new list that is the reverse of the one passed

#lost. what am I having issue with? #what we've learned e.g. the syntax, what it does and how to combine

#short cut

def reverse_list_2(my_list):
    return my_list[::-1]

#print(reverse_list_2([2, 4, 6, 8, 10]))


#check if my_string is a palindrome return true if it is, False otherwise
#level is for example a palindrome or aaa, racecar
# l e v e l
# 0       len -1
#research idx

'''

'''

def is_palindrom(my_string):
    for idx in range(len(my_string)):
        if my_string[idx] == 

'''



def reverse(my_string):
   reversed_string = ''
   for idx in range(len(my_string) - 1, -1, -1):
       reversed_string += my_string[idx]
   return reversed_string
def is_palindrome(my_string):
   '''
   check if my_string is a palindrome
   return True if it is, False otherwise
   '''
   backwards = reverse(my_string)
   if backwards == my_string:
       return True
   return False


print(is_palindrome('level'))
print(is_palindrome('racecar'))
print(is_palindrome('aaa'))
print(is_palindrome('aaadba'))
print(is_palindrome('amanaplanacanalpanama'))


#the game has two players
#each player has to be able to roll the die
#they can roll again or hold their score and pass a turn to another player
#has to be able to record current score
#each roll gets added to the players current score
#if player rolls a 1, the player looses a turn and the total score for the player resets to 0
#first to 100 wins
#be able to tell who's turn it is
#score for round is different from total score



player1 = 0
player2 = 1

for in 
player_one_score
player_two_score
turn
current_score

max_score = 20

while True

#try solving for roll
#player 1 rolls 
#player 2 rolls


import random



for in 


current_score = 

player1 = random.randint(1, 6)
        return sum
player2 = random.randint(1, 6)
        return sum
if randint + sum


player1_total
player2_total

r = roll
h = hold





    
