# map function
# The map function allows you to "map" a function to an iterable object. That is to say you can quickly call the same function to every item in an iterable, such as a list. For example:

def square(num):
    return num**2
print(square(45))

my_nums = [1,2,3,4,5]
print(list(map(square,my_nums)))

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'even'
    else:
        return mystring[0]
mynames = ['John','Cindy','Sarah','Kelly','Mike']
print(list(map(splicer,mynames)))


# filter function
# The filter function returns an iterator yielding those items of iterable for which function(item) is true. Meaning you need to filter by a function that returns either True or False. Then passing that into filter (along with your iterable) and you will get back only the results that would return True when passed to the function.

def check_even(num):
    return num % 2 == 0 
nums = [0,1,2,3,4,5,6,7,8,9,10]
filter(check_even,nums)
print(list(filter(check_even,nums)))


#lambda expression
#lambda's body is a single expression, not a block of statements.

def square(num):
    result = num**2
    return result
print(square(7))   # thats simple 

# but wit one line function 
def square(num): return num**2
print(square(8))  # thats one line

#with lambda fuction 

lambda num: num ** 2
# You wouldn't usually assign a name to a lambda expression, this is just for demonstration!
square = lambda num: num **2
print(square(6))


#lambda with map and filter 
print(list(map(lambda num: num ** 2, my_nums)))
print(list(filter(lambda n: n % 2 == 0,nums)))

#Nested Statements and Scope

x = 25

def printer():
    x = 50
    return x

# print(x)
print(printer())
# What do you imagine the output of printer() is? 25 or 50? What is the output of print x? 25 or 50?

print(x)

# local
# enclosing functions
# global
# built-in


# Local
# x is local here:
f = lambda x:x**2

# Enclosing function locals

name = 'This is a global name'

def greet():
    # Enclosing function
    name = 'Sammy'
    
    def hello():
        print('Hello '+name)
    
    hello()

print(greet()) #enclosion

print(name) # global
print(len) #built in 

#local variable 
x = 50

def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

func(x)
print('x is still', x)

# global variable 

x = 50

def func():
    global x
    print('This function is now using the global x!')
    print('Because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to', x)
print('Before calling func(), x is: ', x)
func()
print('Value of x (outside of func()) is: ', x)







