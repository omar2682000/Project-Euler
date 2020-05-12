l=[]
for i in range(20):
    l.append(list(map(int,input().split())))
m=0
for i in range(20):
    m1,m2,m3,m4=0,0,0,0
    for j in range(20):
        if j<=16:
            m1=l[i][j]*l[i][j+1]*l[i][j+2]*l[i][j+3]
        if i<=16:
            m2=l[i][j]*l[i+1][j]*l[i+2][j]*l[i+3][j]
        if i<=16 and j<=16:
            m3=l[i][j]*l[i+1][j+1]*l[i+2][j+2]*l[i+3][j+3]
        if i<=16 and j>=3:
            m4=l[i][j]*l[i+1][j-1]*l[i+2][j-2]*l[i+3][j-3]
        if max(m1,m2,m3,m4)>m:
            m=max(m1,m2,m3,m4)
print(m)
"""
Very boring problem, simple implementaion problem, all you have to do
    is a brute force solution, actually, I don't know how I didn't 
    lazy and ignored the code as I could solve the problem's idea
    from the first 10 seconds, nothing to learn from it.
"""
