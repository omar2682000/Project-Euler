for t in range(int(input())):
    n  , k = map(int , input().strip().split());
    arr = input();
    arr = [int(i) for i in arr];
    solutions = []
    answer = 0
    l , r = 0 , k;
    while r <= n:
        solutions.append(arr[l : r]);
        l += 1;
        r += 1;
    for i in solutions:
        pivot = 1;
        for j in i : 
            pivot *= j;
        if pivot > answer : answer = pivot;
    print(answer)
"""
Very boring problem, I used 2-Pointers techniqe in oreder to solve it,
    nothing hard at all, no knowledge of math is required, just implement
    the techniqe and go ahead,,, I'm disappointed to be honest, it started 
    to become boring, hope harder problems are waiting for me.
"""
