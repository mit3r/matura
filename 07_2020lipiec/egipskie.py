

# ulamek egipski 1/m  dla m > 1


# algorytm min(n) >= a^-1, ulamek 1/n 


# r =  a - 1/n if r == 0 good else repeat with r


import math

def find_egipt(p, q, rozklady):

    n = math.ceil(q / p)

    r_licz, r_mian = p * n - q, q * n

    if r_licz == 0:
        return rozklady + [n]

    return find_egipt( r_licz, r_mian, rozklady + [n]) 

if __name__ == '__main__':
    dane = [
        [4, 5],
        [8, 15],
        [5, 6],
    ]

    for l, m in dane:
        print(l, m, find_egipt(l, m, []))