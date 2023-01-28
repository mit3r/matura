

def f(n):

    if n == 0:
        return 1
    
    s = 1
    for i in range(n):
        s = s + f(i)
    
    return s


n = 10

print(n, f(n))

# P F F P