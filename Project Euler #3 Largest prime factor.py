from math import sqrt
T = int(input())
for t in range(T):
    n = int(input())
    i=2
    while i<=sqrt(n):
        while( n%i == 0 and n != i ):
            n=n//i
        i += 1
    print(n)
"""The key to solve this problem is to realize 4 facts :-
      1- You do not need to go through all numbers from 2 to n, all you need is those between 1 and sqrt(n).
      2- Considering the Prime Number definition, as it is only divisible by 1 and itself, then you must factorize n 
            until you reach a number that is a prime number.
      3- You must handle 2 edge cases :-
          Case #1 : n is prime.
          Case #2 : n is a perfect square.
      4- Every integer number can be written as a product of prime numbers, as n > 9, cases that n = 1 or 0 which are 
            special cases are ignored, also that the answer exists whatever the n's value is"""
