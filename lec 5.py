# Functions
# creating and calling function 

def func_1():
    print('Fuction is created ')
func_1()

def add_func(num1,num2):
    return num1+num2
result = add_func(input(),input()) # used multiple inputs because in python input function takes only one input at once
print('Sum of arguments passed is  : ',result)

# function with logic 

def even_check(num):
    result =num%2==0
    return result
print( even_check(int(input())))

def even_check_from_list(num_list):
    for num in num_list:
        if num%2==0:
            return True
        else:
            pass
print(even_check_from_list([1,3,5,7,3,3]))


#interaction between function  and making a game

list_1 =[1,2,3,4,5,6,7,8,9]
from random import shuffle
shuffled_list=shuffle(list_1) # as its not returning anything so we write further code for this
print (list_1)

def list_shuffling(new_list):
    shuffle(new_list)
    return new_list

# print(list_shuffling(list_1))
new_list = ['','O','']
print(list_shuffling(new_list))

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess=input('Pick a number from : 0, 1 or 2 : ')
    return int(guess)
# print(player_guess())

# now we check the players guess if its correct or not 
def  check_player_guess(new_list, guess):
     if new_list[guess]=='O':
        print('Correct guess')
     else:
        print('Wrong guess')
        print(new_list)
guess=player_guess()
mixedup_list= list_shuffling(new_list)
print(check_player_guess(mixedup_list, guess))

#args and keyword arguments

def myfunc(a,b):
    return sum ((a,b))* 0.05

print(myfunc(30,40)) # we can add more numbers but we have to add same more arguments in func

#for multiple as many as wants we have to use 

def myfunc_1(*args):
    return sum ((args))* 0.05
print(myfunc_1(30,40,5,7,89)) # in this we can add as many as we want we can any keyword with * on the place of args

# now with keyword arguments

def my_func_new(**kwargs):
    if 'vegitable' in kwargs:
        print( "My vegitable choice  {}".format(kwargs['vegitable']))
    else:
        print('No vegitables found in it  ')
    return ''
print(my_func_new(fruite='apple',vegitable=('mushrooms','uroom'))) 
# The difference between them is the single *args returs the tuple or list where duble **kwargs returns a dictionary 

# we can use both in same program like 
def my_funcforboth(*args,**kwargs):
    print( "My vegitable choice  {} {}".format( args[1],kwargs['vegitable']))
print(my_funcforboth(1,3,5,7,8,10,fruite='apple',vegitable=('mushrooms','uroom'))) 


