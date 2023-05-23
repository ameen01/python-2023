#----------------------------------------------------------

#You have been given a list of names. Your task is to iterate over
#the list and print only the names that start with the letter 'A'.

# names = ['hadil','hamodi','lara', 'ameen','mayada','rian']

#1)
# for name in names:
#     if name.startswith('a'):
#         print(name ,'start with a ')

# #2)
# for name in names:
#     if name[0] == 'a':
#         print(name ,'start with a too')
        
    
#----------------------------------------------------------

#Write a program that takes a list of numbers as input and calculates the 
# sum of all the positive numbers in the list. The program should then print the sum.
numbers = [-4,-30,-2,-1,0,1,2,3,59,5]

sum_positive_numbers = 0
for num in numbers:
    if num < 0:
        sum_positive_numbers +=num

print(sum_positive_numbers)

#___________________________________________________________________
#Write a program that takes a list of strings as input, and outputs 
# the length of the longest string in the list.
names = ['hadil','hamodi','lara', 'ameen','mayada','rian', 'miryam','habil']
how_long = 0

for name in names:
    if len(name) > how_long:
        print(len(name))