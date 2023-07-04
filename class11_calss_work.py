## range ---https://www.w3schools.com/python/ref_func_range.asp
# print(range(10))
# for x in range(10):
#     print(x)

# print("-------------")

# for x in range(1,11):
#     print(x)


# print('-----------3')
# for x in range(1,12,2):
#     print(x)

# #_____________________________________
# whlie loop
#https://www.w3schools.com/python/python_while_loops.asp
# i = 1
# while i < 10:
#     print(i)
#     i +=1

# while True:
#     print("*")

#_____________________________________________
#function
#https://www.w3schools.com/python/python_functions.asp

def my_function():
    print('ameen')

my_function()


def sec_function(name):
    print(name)

# sec_function('lara')
# sec_function('hadil')


# def names(fname,lname):
#     print(f'my name is {fname}. and my last name is {lname} ')

# names('ameen','adam')

def names(fname,lname):
    info = f'my name is {fname}. and my last name is {lname}'
    return info


x= names('ameen','adam')
print(x)

# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()