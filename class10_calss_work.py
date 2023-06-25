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


# Write a function that calculates the sum of all the numbers 
# from 1 to a given integer, but only if the number is greater
# than 0.

# write a function that takes three numbers as parameters and
#  returns the largest among them.



