def sum3(n : int): return ( n / 2 ) * (6 + ( 3 * ( n - 1 )))
def sum5(n : int): return ( n / 2 ) * (10 + ( 5 * ( n - 1 )))  
def sum15(n : int): return ( n / 2 ) * (30 + ( 15 * ( n - 1 ))) 
'''Use Arithmetic Progression sum to find the multiples of 3,5 & 15'''
for i in range(int(input())):
    N = int(input())
    N -= 1
    three = N//3  
    five = N//5
    fifteen = N//15
    print( ( sum3(three) + sum5(five) ) - sum15(fifteen) )
    '''As long as 15,30...etc are multiples of both 3 & 5 ,then it will be added 2 times to the sum so we subtract it once'''
