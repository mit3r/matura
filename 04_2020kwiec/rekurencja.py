
T = {i+1: v for i, v in enumerate([1,5,8,10,12,14,19,20,23,30,38])}

def Rek(x, p, k):
    # print(x, p, k)
    global T

    if p < k:
        s = (p + k) // 2

        if T[s] >= x:
            return Rek(x, p, s)
        
        return Rek(x, s + 1, k)

    if T[p] == x:
        return p
    
    return -1

Rek(7, 1, 11)

# 2020 5 14 s = 9
# 2020 5 9 s = 7 
# 2020 5 7 s = 6
# 2020 5 6 s = 5
# 2020 5 5

# najwięcej 5 wywołań

T = {9: 0, 12: 0, 13: 0}

# 2020 5 14
#   s = 9
# 2020 10 14
#   s = 12
# 2020 13 14
#   s = 13
# 2020 14 14
# koniec

# najmniej 4 wywołań

# odpowiedz 4, 5
