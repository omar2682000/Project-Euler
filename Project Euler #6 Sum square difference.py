for t in range(int(input())):
    n = int(input());
    
    sum_1 = pow(int(n * (n + 1) / 2) , 2); 
"""
sum_1 here uses Arithmetic Progression formula < (n * (n + 1) / 2) > to find
    the summation of all numbers in the renge [ 1 , n ], then squares it.
"""    
    sum_2 = int(n * (n + 1) * ((2 * n) + 1) / 6);
"""
sum _2 uses the formula < ((k+1)(k+2)(2(k+1)+1) / 6) > to find the summation of
    sqares of all numbers in the range [ 1 , n ].
"""    
    print(abs(sum_1 - sum_2));
"""
Finally we print the absolute difference for both summations,
    actually this problem takes some basic knowledge about
    sequences in order to solve, easy boring one to be honest.
"""
