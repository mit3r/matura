


def silnia(n):

    if n == 0:
        return 1

    w = 1
    while n > 0:
        w *= n
        n -= 1

    return w


def nwd(a,b):
    while b:
        a, b = b, a%b
    
    return a

if __name__ == '__main__':

    liczby = [ int(line.strip()) for line in open('liczby.txt', 'r') ]


    print('Zad. 4.1')
    potegi3 = [False for i in range(0, 100_000+1)]
    i = 1
    while i <= 100_000:
        potegi3[i] = True
        i *= 3
    
    odp = 0
    for current in liczby:
        if potegi3[current]:
            odp += 1

    print(odp)

    print('Zad 4.2')
    suma_silni = lambda n: sum([*map(silnia, [*map(int, str(n))])])

    rowne_silni = [n for n in liczby if n == suma_silni(n)]
    print(rowne_silni)


    print('Zad 4.3')

    temp = {
        'start': 0,
        'end': 0,
        'dl': 1,
        'nwd': liczby[0]
    }
    maks = temp.copy()

    i = 0
    for i, current in enumerate(liczby):
        
        temp['nwd'] = nwd(temp['nwd'], current)
        if temp['nwd'] <= 1:
            temp['nwd'] = current
            temp['start'] = i-1
            temp['end'] = i-1
            temp['dl'] = 1

            continue

        temp['end'] = i
        temp['dl'] = temp['end'] - temp['start'] + 1

        if maks['dl'] < temp['dl']:
            maks = temp.copy()
        
        
    print(liczby[maks['start']], maks['dl'], maks['nwd'])
        







    

