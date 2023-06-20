# make a calcuator with all what we learnd so far 
# input ,str, int ,float ,for loop ,if 
#______________----__________
print('1) add')
print('2) sub')
print('3) multi')
print('4) div')

usr_input = input('type your choice:')
if usr_input.isalpha():
    print('not a number')
else:
    usr_input = int(usr_input)
    if usr_input <=4:
        if usr_input ==1:
            num1 = int(input('number '))
            num2 = int(input('sec number'))
            print(num1+num2)
