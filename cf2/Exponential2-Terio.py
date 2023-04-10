import math, sys

def mod_pow(a, b, m): # function to calculate a^b modulo m efficiently
    result = 1 # initialize result to 1
    while b > 0: # while b is greater than 0 
        if b % 2 == 1: # if b is odd
            result = (result * a) % m # multiply result by a modulo m
        a = (a * a) % m # multiply a by a modulo m
        b //= 2 # divide b by 2
    return result # return result

n = int(input()) # read the input values
for i in range(n): # for each input value
    a, b, c = map(int, input().split()) # read the input values
    
    # Calculate b^c modulo phi(m)
    phi = 10**9 + 6 # phi(m) = m - 1
    exp = mod_pow(b, c, phi) # calculate b^c modulo phi(m)
    
    # Calculate a^(b^c) modulo m using modular exponentiation
    m = 10**9 + 7 # m = 10^9 + 7
    result = mod_pow(a, exp, m) # calculate a^(b^c) modulo m
    print(result) # print the result
