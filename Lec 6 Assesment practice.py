# Question no.1 

def vol(radius):
    pi = 3.14159 # you can also use math.pi for more accurate value of pi
    volume = (4/3) * pi * (radius ** 3)
    return volume
print(vol(2))

# Question no.2

def ran_check(num, low, high):
    return num >= low and num <= high
print(ran_check(5,2,7)) 

# If you want boolean

def ran_bool(num, low, high):
    return low <= num <= high
print(ran_bool(3,1,10))


# Question no.3

def count_case(string):
    uppercase_count = 0
    lowercase_count = 0
    for char in string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
    print(f'No. of Upper case characters: {uppercase_count}')
    print(f'No. of Lower case characters: {lowercase_count}')
print(count_case('Hello Mr. Rogers, how are you this fine Tuesday?'))

# Question no.4 

def get_unique_list(input_list):
    return list(set(input_list))
input_list = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]
unique_list = get_unique_list(input_list)
print(unique_list)

# Question no.5

def multiply_list_numbers(input_list):
    result = 1
    for num in input_list:
        result *= num
    return result
input_list = [1, 2, 3, -4]
result = multiply_list_numbers(input_list)
print(result)


# Question no. 6

def is_palindrome(string):
    # Convert the string to lowercase and remove spaces
    string = string.lower().replace(" ", "")
    
    # Reverse the string and compare it to the original string
    return string == string[::-1]
print(is_palindrome("racecar")) 
print(is_palindrome("helleh"))

# # Question No. 7

import string

def is_pangram(str):
    str = str.lower().replace(" ", "")
    #str = str.lower().replace(int, "")
    str = str.lower().replace(".,/:;'[]{]}\|=+-_*&^%$#@`~","")
    unique_chars = set(str)
    if unique_chars == set(string.ascii_lowercase):
      return  True
    else:
        return False
print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("hello"))



import string
 
def is_pangram(str):
    unique_char = "abcdefghijklmnopqrstuvwxyz"
    for char in unique_char:
        print(char)
        if char not in str.lower():
            return False
        else:
            return True
    if(is_pangram(string) == True):
        return True
    else:
        return False
print(is_pangram("4563456The quick brown fox jumps over the lazy dog"))
print(is_pangram("hello"))
