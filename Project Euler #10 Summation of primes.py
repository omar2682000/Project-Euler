def sieve():
    numbers = [True for i in range(pow(10 , 6))];
    numbers[0] = False;
    numbers[1] = False;
    for i in range(2 , len(numbers)):
        j = i * i;
        while (j < len(numbers)):
            numbers[j] = False;
            j += i;
    return [i for i in range(len(numbers)) if numbers[i] is True];
primes = sieve();
for t in range(int(input())):
    n = int(input());
    ans = 0;
    for i in primes : 
        if i > n : break;
        ans += i;
    print(ans)
"""
-----------------------------------------------------------------------------------------------------
| Another boring problem, but I can say it can teach me a lot if I know nothing about Prime Numbers |
-----------------------------------------------------------------------------------------------------
No need for any clarification here, you can go back for < Project Euler #7 10001st prime >
    solution as it has the same idea about generating Prime Numbers in a fast way.
    
"""
