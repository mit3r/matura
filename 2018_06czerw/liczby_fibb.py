

def F_rek(n):

    if n in [1,2]:
        return 1
    
    return F_rek(n-1) + F_rek(n-1)


def F_iter(n):

    if n in [1,2]:
        return 1

    p, q = 1, 1
    i = 2
    while i < n:
        p, q = q, p+q
        i += 1
    
    return q

def F_rb(n):

    if n in [1,2]:
        return 1
    
    if n % 2 == 0:
        k = n // 2
        return F_rb(k + 1)**2 - F_rb(k -1)**2
    
    else:
        k = (n+1) // 2
        return F_rb(k)**2 + F_rb(k-1)**2

print(F_iter(45))
print(F_rb(45))
