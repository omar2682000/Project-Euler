T = int(input())
for t in range(T):
    f1 , f2 , f3 , c , ans = 1 , 1 , 2 , 3 , 0
    n = int(input())
    while f3<n : 
        if c % 3 == 0 : ans += f3 """The key to solve this problem is this line """
        """You can simply realize that you get an even nember every 3 numbers (it's the 3rd one)"""
        c += 1
        f1 = f2
        f2 = f3
        f3 = f1 + f2
        """generate Fibonacci Numbers using the formula F(n) = F(n - 1) + F(n - 2)"""
    print(ans)
