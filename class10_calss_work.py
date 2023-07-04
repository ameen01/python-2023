# write a function that takes two strings as parameters
# and checks if they have the same length.
def my_function(a,b):
    if len(a) == len(b):
        print(a,'and',b,' are the same length.' )
    else:
        print(a,'and',b,' are Not the same length.' )

my_function('home','amen')
my_function('hadil','lara')

# write a function that takes a list of integers as input and 
# returns a new list containing only the even numbers from the 
# original list.

def even_function(z):
    z = list(z)
    new_list =[]
    for x  in z:
        if x %2 == 0:
            new_list.append(x)
    print(new_list)

my_list = [1,2,3,4,5,6,7,8,9]
even_function(my_list)

# write a function that takes a list of words as input and 
# returns a new list containing only the words with more than
# 5 characters.

def word_function(word_list):
    word_list = list(word_list)
    new_list2 = []
    for word in word_list:
        if len(word) > 5:
            new_list2.append(word)
    print(new_list2)

names =['ameen', 'lara','mayada','hadil']
word_function(names)



# Write a function that calculates the sum of all the numbers 
# from 1 to a given integer, but only if the number is greater
# than 0.

def sum_all(a):
    sum = 0
    if a == 0:
        print('cant use this number ')
    else:
        for x in range(1,a):
            sum +=x
    print(sum)

sum_all(8)
# write a function that takes two numbers as parameters and
#  returns the largest among them.
def largest(x,z):
    if x > z:
        print(x, 'the largest number')
    else:
        print(z, 'is the largest')

largest(5,6)
