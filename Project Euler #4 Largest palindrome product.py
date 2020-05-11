T = int(input());

def isPalindrome(string : str):
    if (string == string[::-1]):return True;
    else : return False;
    """This Function checks if the string it is given is Palindrome or not"""
    
def generate():
    arr = []
    for i in range(100 , 1000):
        for j in range(100 , 1000):
            string2 = str(i * j)
            if (isPalindrome(string2)):arr.append(i * j);
    arr.sort();
    return arr;
    """This Function here uses a the first part of my Brute Force idea
            to generate all possible solutions"""
def find_answer(n , arr):
    for i in range(len(arr)):
        if arr[i] >= n : return i - 1;
    """This function completes the other part of the idea to return an index for
            the first palindromic number less than n"""
    
solutions = generate();

for t in range(T):
    n = int(input());
    print(solutions[find_answer(n , solutions)])
    
"""
Nothing weird about this problem, it migh look tricky at the first momment, 
        but once you think about the limits you have, you will realize
        that it's okay to go Brute Force (This solution won't pass all cases
                                            if limits were sharper)
        but anyway, that's a solved problem now
        Also, a wise friend of mine said once : xD
"""
