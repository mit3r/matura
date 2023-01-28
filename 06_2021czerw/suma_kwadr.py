



def rep_kwadrat(n):

    suma = 0
    i = int(pow(n, 1/2))

    kwadraty = []

    while suma != n:

        if i**2 + suma <= n:
            kwadraty += [i]
            suma += i**2
        else:
            i -= 1
    
    return kwadraty


for i in [2, 5, 8, 12, 16]:
    print(rep_kwadrat(i))