T = int(input());
def isPalindrome(string : str):
    if (string == string[::-1]):return True;
    else : return False;
def generate():
    arr = []
    for i in range(100 , 1000):
        for j in range(100 , 1000):
            string2 = str(i * j)
            if (isPalindrome(string2)):arr.append(i * j);
    arr.sort();
    return arr;
def find_answer(n , arr):
    for i in range(len(arr)):
        if arr[i] >= n : return i - 1;
solutions = generate();
for t in range(T):
    n = int(input());
    print(solutions[find_answer(n , solutions)])
