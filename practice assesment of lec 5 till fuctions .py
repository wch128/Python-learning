def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)
print(lesser_of_two_evens(2,5))

def animal_crackers(text):
    words = text.split()
    return words[0][0] == words[1][0]
print(animal_crackers('Crazy Kangaroo'))

def makes_twenty(n1, n2):
    if n1 == 20 or n2 == 20 or n1 + n2 == 20:
        return True
    else:
        return False
print(makes_twenty(2,3))

def old_macdonald(name):
    first_letter = name[0].upper()
    inbetween = name[1:3]
    fourth_letter = name[3].upper()
    rest = name[4:]
    return first_letter + inbetween + fourth_letter + rest
print(old_macdonald('macdonald'))

def master_yoda(text):
    words = text.split()
    words_reversed = words[::-1]
    return " ".join(words_reversed)
print(master_yoda('We are ready'))

def almost_there(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)
print(almost_there(209))

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
print(has_33([3, 1, 3]))


def paper_doll(text):
    result = ""
    for char in text:
        result += char * 3
    return result
print(paper_doll('Mississippi'))

def blackjack(a, b, c):
    sum = a + b + c
    if sum <= 21:
        return sum
    elif sum > 21 and 11 in [a, b, c]:
        sum -= 10
        if sum <= 21:
            return sum
        else:
            return 'BUST'
    else:
        return 'BUST'
print(blackjack(9,9,11))

def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        if num == 6:
            add = False
        if add:
            total += num
        if num == 9:
            add = True
    return total
print(summer_69([2, 1, 6, 9, 11]))

def spy_game(nums):
    code = [0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)  
    return len(code) == 1
print(spy_game([1,7,2,0,4,5,0]))

def count_primes(num):
    if num < 2:
        return 0
    primes = [True] * (num + 1)
    p = 2
    while p * p <= num:
        if primes[p] == True:
            for i in range(p * 2, num + 1, p):
                primes[i] = False
        p += 1
    return sum(primes[2:])
print(count_primes(100))


def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   *',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])
print(print_big('a'))