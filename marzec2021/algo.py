

liczba = 0

def Algo(n):
    global liczba
    liczba = 0

    if n <= 2:
        return 1
    
    p = 1
    k = n

    while k - p > 1:
        s = (p + k) // 2
        liczba += 1
        if s * s <= n:
            p = s
        else:
            k = s
    
    return p




if __name__ == '__main__':

    dane = [5, 2, 63, 1024]

    for n in dane:
        print('n:', n, Algo(n), liczba)