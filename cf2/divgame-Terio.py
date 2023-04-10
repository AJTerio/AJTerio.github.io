import math, sys

'''
Problem Statement
Given is a positive integer N. 
Consider repeatedly applying the operation below on N:
First, choose a positive integer z satisfying all of the conditions below:
z can be represented as 
z = p^e, where p is a prime number and e is a positive integer;
z divides N;
z is different from all integers chosen in previous operations.
Then, replace N with N/z.
Find the maximum number of times the operation can be applied.
'''

def is_prime(n): # returns True if n is prime, False otherwise
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1): # only need to check up to sqrt(n)
        if n % i == 0: # if n is divisible by i, then n is not prime
            return False # so return False
    return True # if n is not divisible by any i, then n is prime

def max_operations(n): # returns the maximum number of times the operation can be applied
    primes = [] # list of primes that have been used
    while n != 1: # while n is not 1 
        found = False # flag to indicate if a prime has been found
        for i in range(2, n + 1): # check all numbers from 2 to n
            if is_prime(i) and n % i == 0 and i not in primes: # if i is prime, i divides n, and i has not been used
                primes.append(i) # add i to the list of primes that have been used
                e = 1 # exponent
                while n % (i**e) == 0: # find the largest power of i that divides n
                    e += 1 # increment e
                n //= (i**(e - 1)) # divide n by the largest power of i that divides n
                found = True # set flag to True
                break # break out of for loop
        if not found: # if no prime has been found
            break # break out of while loop
    return len(primes) # return the number of primes that have been used

def main(): # main function to call the max_operations function
    print(max_operations(24)) # answer should be 3
    print(max_operations(1)) # answer should be 0
    print(max_operations(64)) # answer should be 3
    print(max_operations(1000000007)) # answer should be 1
    print(max_operations(99764507000)) # answer should be 7

main() # call main function