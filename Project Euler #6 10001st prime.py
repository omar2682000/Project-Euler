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
for t in range(int (input()) ):
    n = int(input());
    print(primes[n - 1]);
"""
It's a very basic Number Theory problem, all you have to do in order to solve
    this problem is to use some fast algorithm to generate the first 
    10^4 Prime numbers,in my case I used the < Sieve of Eratosthenes >
    Algorithm with complexity close to O(n*log(n)).
"""
