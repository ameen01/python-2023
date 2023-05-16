#----------------------------------------------------------

#You have been given a list of names. Your task is to iterate over
#the list and print only the names that start with the letter 'A'.

names = ['hadil','hamodi','lara', 'ameen','mayada','rian']

#1)
for name in names:
    if name.startswith('a'):
        print(name ,'start with a ')

#2)
for name in names:
    if name[0] == 'a':
        print(name ,'start with a too')
        
    
#----------------------------------------------------------

#Write a program that takes a list of numbers as input and calculates the sum of all the positive numbers in the list. The program should then print the sum.
#Write a program that takes a list of strings as input, and outputs the length of the longest string in the list.
