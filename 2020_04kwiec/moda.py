
# z = [0, 1, 1, 1, 3, 3, 3, 4, 4, 4]

def maksimum(n, tab):
    maks = tab[0]

    for i in range(0, n):
        if tab[i] > maks:
            maks = tab[i]
    
    return maks

def gdzie(e, n, tab):

    for i in range(0, n):
        if tab[i] == e:
            return i
    
    return -1

def moda(n, tab):

    keys = []
    values = []

    for i in range(1, n+1):

        pos = gdzie(tab[i], len(keys), keys)
        if pos != -1:
            values[pos] += 1
        else:
            keys += [tab[i]]
            values += [1]

    maks = maksimum(len(values), values)

    for i in range(0, n):
        if values[i] == maks:
            return keys[i]


z = [7, 3, 3, 7, 7, 8, 0]

z = {i+1: v for i, v in enumerate(z)}
        
print(moda(len(z), z))

