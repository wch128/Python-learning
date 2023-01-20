print ('Python objects and data structure basics')
print ('deta types')
# int 
# float 
# str 
# list 
# dict
# tuple
# set
# bool
# python using dynamic datatypes 

my_cars = 2
my_cars =["suzuki","toyota"]
print (my_cars)
# type checking in code by variables
a=20
b=3.5
type (b)

#example 
my_salary = 50000
tax_rate = 0.1
my_tax = my_salary * tax_rate
print (my_tax)

# indexing and slicing string

#indexing 
mystring = " My name is Waqas Arif "
print(mystring[1])
print(mystring[4:18])
print(mystring[:18])
print(mystring[:])

#slicing
print(mystring[::3])
print(mystring[::-1])

#immutability 

name = "Waqas Arif"
print(name)
new_name= name[0:4]+"r"
print(new_name)
#its kinda concatination
print( name.upper())
print(name.split())
print(name.split('a'))
print('salry of Waqas is {}'.format(my_salary)) #print formatting with string
print(f'salry of {new_name} is {my_salary}')


#with list method 

my_list =['one','two','three']
number_list=[1,2,3,4,6,5,9,8,7]
print(my_list+number_list[::-1])
print(my_list[::-1]+number_list[::-1]) #indexing , slicing , concatination with list 
my_list[1]=number_list[1]
my_list.append('four')
print(my_list)
my_list.pop()
print('list after pop',my_list)
number_list.sort() #sorting 
print(number_list)
number_list.reverse() #reversing 
print(number_list)

#Dictionaries

# take the example of an autoparts store
store ={'mobil oil':2300,'break oil':500,'crude oil':200}
#oil = input() #used this for input logic 
print('Mobil oil', ' ', store['mobil oil']) #turn "Mobil oil into oil on both instence for input method"

store_list2 ={'oils':300,'bumpers':[20,30,15],'keys':30} #dictionary with list 
print(store_list2['bumpers'])
print(store_list2['bumpers'][1]) #dictionary with list using index searching from list 

#tuples

t=(1,2,3,4,5,5,5,6,6)
print(type(t))
print(len(t))
print('count is qual to ',t.count(5))
print('index is qual to ',t.index(3))

#sets

my_set = set()
my_set.add(1)
print (my_set)
my_set.add(2)
print (my_set)
new_set={1,2,4,5}
print ('intersection of these sets is ', my_set.intersection(new_set))

#booleans 

# simply True False
a=1>2
b=2==2
print(a)
print(b)

#files I/O

writefile=open('myfile.txt','w')
writefile.write('Hi how are you doing?')
writefile.close()

writefile = open('myfile.txt','r')
print(writefile.read())
print(writefile.seek(1)) #will read the file form the index that you will be enter but remember the index will start from 0
print(writefile.read())


# next i just solved the assesment for today attched as the juypetr notebook file 

