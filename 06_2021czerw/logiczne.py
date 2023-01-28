



def W(a,b):
    return 1 if ((not a) and b) or (a and (not b)) else 0

dane = [
    [0,0],
    [1,0],
    [0,1],
    [1,1],
]

for a,b in dane:

    print(W(a,b))