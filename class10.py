#https://www.w3schools.com/python/python_functions.asp
#A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
#Afunction can return data as a result.


# def my_function():
#     print('welcome to ptyhon'.capitalize())


# my_function()
# my_function()


# def add():
#     x = 47734
#     y = 25374
#     print(x+y)

# add()

def sub(x):
    print(x-10)

sub(11)
# sub(1000,888)

# def my_function(x,y):
#     my_list = [1,3,4,5,6,7,8,10]
#     my_list.insert(1,x)
#     my_list.insert(8,y)
#     for x in my_list:
#         print(x)

# my_function(2,9)

# ODD_OR_EVEN 
def odd_or_even(x):
    if x % 2 == 0:
        print(x, 'is an even number')
    if x % 2 != 0:
        print(x,'is an odd number')

odd_or_even(6)
odd_or_even(3)


for y in range(50):
    odd_or_even(y)