def myfunc(a,b):
    return sum((a,b))*.05

print(myfunc(40,60))

# simple function
def myfunc(a=0,b=0,c=0,d=0,e=0):
    return sum((a,b,c,d,e))*.05

print(myfunc(40,60,20))

# *args

#When a function parameter starts with an asterisk, it allows for an arbitrary number of arguments, and the function takes them in as a tuple of values. Rewriting the above function:

def myfunc(*args): # it always used with single staric *
    return sum(args)*.05

print(myfunc(40,60,20))
#Notice how passing the keyword "args" into the sum() function did the same thing as a tuple of arguments.

# **kwargs

# Python offers a way to handle arbitrary numbers of keyworded arguments. Instead of creating a tuple of values, **kwargs builds a dictionary of key/value pairs

def myfunc(**kwargs): #it always used wit doubble staric **
    if 'fruit' in kwargs:
        print(f"My favorite fruit is {kwargs['fruit']}")  # review String Formatting and f-strings if this syntax is unfamiliar
    else:
        print("I don't like fruit")
        
print(myfunc(fruit='pineapple'))


print(myfunc()) # now the result will be changed


# *args and **kwargs combined

# can pass *args and **kwargs into the same function but *args have to appear before **kwargs

def myfunc(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass
        
print(myfunc('eggs','Breads',fruit='cherries',juice='orange'))

