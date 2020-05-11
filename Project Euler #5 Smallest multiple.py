from math import gcd 
def lcm(a , b):return (a * b) // gcd(a , b);

"""
This Function called lcm returns the leatest common multiple of 2 numbers
      << You can do it using recursion with the formula lcm(lcm(a , b) , c)
            to avoid some kind of overflow , but it's okay as n's value 
            can not exceed 40 >>
"""

for t in range(int(input())):
    n = int(input());
    for i in range(2 , n) : n = lcm(n , i);
    print(n)
    
"""
The kye behind this problem (which is a Number Theory problem by the way) is 
        understanding both (lcm & gcd), nothig weird, just another simple boring
        problem, but it's okay so far as we are still at first few problems, I 
        think it's a natural thing so far.
"""
