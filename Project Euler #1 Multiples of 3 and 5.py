def sum3(n : int): return ( n / 2 ) * (6 + ( 3 * ( n - 1 )))
def sum5(n : int): return ( n / 2 ) * (10 + ( 5 * ( n - 1 )))
def sum15(n : int): return ( n / 2 ) * (30 + ( 15 * ( n - 1 )))
for i in range(int(input())):
    N = int(input())
    N -= 1
    three = N//3
    five = N//5
    fifteen = N//15
    print( ( sum3(three) + sum5(five) ) - sum15(fifteen) )