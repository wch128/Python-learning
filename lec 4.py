# python statements chapter
# use of If Elif Else statement

print('press 1 if need fule  press 2 to start the game ')
a = input()
if a == '1':
    print('Get the fule from station')
elif a == '2':
    print('Game is started')
else:
    print('confirm your fule first ')

# loops
# for loop

count = 0
names = ['talha', 'waqas', 'hamza', 'ashir', 'waqas', 'waqas']
for name in names:
    if name == 'talha':
        count = count + 1
print(count, 'times')
if count == 0:
    print('waqas is not here')
else:
    print('waqas is here')


# while loop 

print('press 1 if need fule  press 2 to start the game ')
a = int(input())
while a == '1':
    print('Get the fule from station')
    a=a+2
while a == '2':
    print('Game is started')
    a=a+3
else:
    print('confirm your fule first ')

# Operator in python 

# Range

my_list = (1,23,3)
for num in range(1,23,3):
    print (num) # range function for itteration 
print (list(( range(1,23,3))))

#index count 

count = 0
words = 'abcdefg'
for word in words:
    print('At index {} the latter is {} '.format(count,word))
    count += 1



words = 'abcdefg'
for word in enumerate (words):
    print(word) # for the form of tuples using enumerate 


# same to print in different way 

words = 'abcdefg'
for word,index in enumerate (words):
    print(index)
    print(word)
    print('\n')

# zip fuction 

my_list =['a','b','c']
num_list =[1,2,3]
big_list =[1000,3500,26700]

for item in zip(my_list,num_list,big_list):
    print (item)  # zip packing

my_list =['a','b','c']
num_list =[1,2,3]
big_list =[1000,3500,26700]

for a,b,c in zip(my_list,num_list,big_list): # zip unpacking
    print (b) # you can change the index to unpack the zipped column

# Min and Max fuction 
num_list2 =(1,3,5,2,7,20,4,9,3,6,8,10)
print (min(num_list2))
print (max(num_list2))

# random library

new_num_list=(1,2,3,4,5,6,7,8,9,10)
from random import shuffle
shuffle(new_num_list)
print(new_num_list)     # with shuffle 

from random import randint
print(randint(0,200))     #with randint


# comprihensions in python

new_string ='Ahmedali'
new_list_3 =[]
for letter in new_string:
    new_list_3.append(letter)
    print(new_list_3) 

new_list_3 =[letter for letter in new_string]
print(new_list_3)
 

# this part is test related code
st = 'Print every word in this sentence that has an even number of letters'
t=st.split()
print (t)
for word in t:
    if len(word)%2==0:
        print(word)



for num in range(1,101):
    if num%3==0:
        print("fizz")
    if num%5==0:
        print("buzz")
    if num%3==0 and num%5==0:
        print("fizzbuss")
    else:
        print(num)

st = 'Create a list of the first letters of every word in this string'
listtest =[latter[0] for latter in st.split()]
print(listtest)

        