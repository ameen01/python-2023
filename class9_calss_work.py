#Write a program that prompts the user to enter a password.
#The program should keep asking for the password until it 
#matches a predefined password.

my_pwd = 12345678
limit = 0
while limit <3: 
    usr_input = input('type your passowrd:')
#    print(type(usr_input))
    usr_input = int(usr_input)
    if my_pwd == usr_input:
        print(f'True, your password is {usr_input}')
    limit +=1





#  Find the largest element in a list using a while loop. 

